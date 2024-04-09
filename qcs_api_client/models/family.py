from enum import Enum


class Family(str, Enum):
    ANKAA = "Ankaa"
    ASPEN = "Aspen"
    FULL = "Full"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
