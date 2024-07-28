__all__ = (
    "Chromosome",
    "ColorConfig",
    "DNAReportInfo",
    "GENOTYPES",
    "GenotypeEntry",
    "Genotype",
)

from enum import StrEnum
from typing import TypedDict


class ColorConfig(TypedDict):
    """Color configuration."""

    A: tuple[int, int, int]
    AA: tuple[int, int, int]
    AC: tuple[int, int, int]
    AG: tuple[int, int, int]
    AT: tuple[int, int, int]
    C: tuple[int, int, int]
    CC: tuple[int, int, int]
    CG: tuple[int, int, int]
    CT: tuple[int, int, int]
    D: tuple[int, int, int]
    DD: tuple[int, int, int]
    DI: tuple[int, int, int]
    G: tuple[int, int, int]
    GG: tuple[int, int, int]
    GT: tuple[int, int, int]
    I: tuple[int, int, int]
    II: tuple[int, int, int]
    T: tuple[int, int, int]
    TT: tuple[int, int, int]

    background: tuple[int, int, int]


class Genotype(StrEnum):
    """DNA genotypes."""

    A = "A"
    AA = "AA"
    AC = "AC"
    AG = "AG"
    AT = "AT"
    C = "C"
    CC = "CC"
    CG = "CG"
    CT = "CT"
    D = "D"
    DD = "DD"
    DI = "DI"
    G = "G"
    GG = "GG"
    GT = "GT"
    I = "I"
    II = "II"
    T = "T"
    TT = "TT"

    NA = "--"


GENOTYPES = tuple(genotype for genotype in Genotype)


class GenotypeEntry(TypedDict):
    """Record of a genotype."""

    genotype: Genotype
    position: int
    rs: str


class Chromosome(TypedDict):
    """Record of a chromosome."""

    label: str
    genotype_entries: list[GenotypeEntry]


class DNAReportInfo(TypedDict):
    """Extracted information about a DNA report."""

    chromosomes_info: dict[str, Chromosome]
    total_entries: int
