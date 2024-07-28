__all__ = ("DNAPNG", "CHROMOSOME_LABELS")

import itertools
import json
import math

import numpy as np
import numpy.typing as npt
from PIL import Image

from dnapng.models import Chromosome, DNAReportInfo, Genotype, GenotypeEntry

NA = "--"

CHROMOSOME_LABELS: tuple[str, ...] = tuple(
    label
    for label in itertools.chain(
        (str(x) for x in range(1, 23)), (x for x in ("X", "Y", "MT", NA))
    )
)


class DNAPNG:
    """Converts a DNA report into a PNG."""

    IMAGE_CHANNELS = 3

    def __init__(
        self,
        dna_report_file: str,
        color_config_file: str,
        genotypes: tuple[Genotype, ...] | None = None,
    ) -> None:
        """Initialize a new DNAPNG instance.

        Args:
            dna_report_file: Path to the DNA report to use.
            color_config_file: Path to the color config file.
            genotypes: The genotypes to paint. If None, then all
                genotypes are painted.
        """
        with open(color_config_file) as f:
            self._color_config: dict[str, list[int]] = json.load(f)

        self._dna_report_info = self._load_dna_report(dna_report_file)
        self._genotypes = genotypes

    @property
    def dna_report_info(self) -> DNAReportInfo:
        return self._dna_report_info

    def displayImage(self) -> None:
        print("Processing...")
        img = self.getImage()
        img.show()
        print("Done.")

    def getImage(self) -> Image.Image:

        sorted_genotype_entries: list[GenotypeEntry] = [
            genotype
            for chromosome in self._dna_report_info["chromosomes_info"].values()
            for genotype in sorted(
                chromosome["genotype_entries"], key=lambda x: x["position"]
            )
        ]

        image_size = math.floor(math.sqrt(self._dna_report_info["total_entries"]))
        print(image_size)

        img: npt.NDArray[np.uint8] = np.zeros(
            (image_size, image_size, self.IMAGE_CHANNELS), dtype=np.uint8
        )
        position = -1
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                position += 1
                genotype_entry = sorted_genotype_entries[position]
                genotype_label = genotype_entry["genotype"]
                if (
                    self._genotypes is not None
                    and genotype_label not in self._genotypes
                ):
                    continue

                r, g, b = self._color_config[genotype_label]
                img[y][x][0] = r
                img[y][x][1] = g
                img[y][x][2] = b

        img = Image.fromarray(img)
        return img

    def _load_dna_report(self, file_path: str) -> DNAReportInfo:
        parsed_chromosomes: dict[str, Chromosome] = {
            label: Chromosome(label=label, genotype_entries=[])
            for label in CHROMOSOME_LABELS
        }

        with open(file_path) as f:
            data = f.readlines()

        entry_count = 0
        for line in data:
            entry_count += 1
            rs, chromosome_label, position, genotype_label = line.split()
            parsed_chromosomes[chromosome_label]["genotype_entries"].append(
                GenotypeEntry(
                    genotype=Genotype(genotype_label),
                    position=int(position),
                    rs=rs,
                )
            )

        return DNAReportInfo(
            total_entries=entry_count, chromosomes_info=parsed_chromosomes
        )
