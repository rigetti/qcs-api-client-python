from enum import Enum


class ValidationErrorIn(str, Enum):
    BODY = "body"
    HEADER = "header"
    PATH = "path"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
