from enum import Enum


class Family(str, Enum):
    NONE = "None"
    FULL = "Full"
    ASPEN = "Aspen"

    def __str__(self) -> str:
        return str(self.value)
