from enum import Enum


class Product(str, Enum):
    QPUJOBCOMPLETION = "qpuJobCompletion"
    QPUJOBTIME = "qpuJobTime"
    RESERVATIONCREATION = "reservationCreation"

    def __str__(self) -> str:
        return str(self.value)
