__all__ = ("DNAPNGArgumentParser", "main")

from tap import Tap

from dnapng.dnapng import DNAPNG
from dnapng.models import GENOTYPES, Genotype


class DNAPNGArgumentParser(Tap):

    dna_report: str
    color_config: str
    genotypes: list[str]

    def configure(self) -> None:
        self.add_argument(
            "-r",
            "--dna-report",
            type=str,
            help="Select the DNA report file to use.",
            required=True,
        )
        self.add_argument(
            "-cc",
            "--color-config",
            type=str,
            help="Select the color configuration file to use.",
            required=True,
        )
        self.add_argument(
            "-g",
            "--genotypes",
            type=str,
            choices=GENOTYPES,
            help=(
                "The genotype (s) you wish the program to paint. If not specified,"
                " then all genotypes are painted."
            ),
            required=False,
        )


def main() -> None:
    args = DNAPNGArgumentParser().parse_args()

    dna_png = DNAPNG(
        args.dna_report,
        args.color_config,
        tuple(Genotype(x) for x in args.genotypes) if args.genotypes else None,
    )

    dna_png.displayImage()
