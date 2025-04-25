from enum import Enum


class NomadJobDatacenters(str, Enum):
    BERKELEY_775 = "berkeley-775"
    FREMONT_FAB = "fremont-fab"
    RIGETTI_GB_1 = "rigetti-gb-1"

    def __str__(self) -> str:
        return str(self.value)
