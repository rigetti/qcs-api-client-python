import datetime
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="Characteristic")


@attr.s(auto_attribs=True)
class Characteristic:
    """A measured characteristic of an operation.

    Attributes:
        name (str): The name of the characteristic.
        timestamp (datetime.datetime): The date and time at which the characteristic was measured.
        value (float): The characteristic value measured.
        error (Union[Unset, float]): The error in the characteristic value, or None otherwise.
        node_ids (Union[Unset, List[int]]): The list of architecture node ids for the site where the characteristic is
            measured, if that is different from the site of the enclosing operation. None if it is the same. The order of
            this or the enclosing node ids obey the definition of node symmetry from the enclosing operation.
        parameter_values (Union[Unset, List[float]]): The optional ordered list of parameter values used to generate the
            characteristic. The order matches the parameters in the enclosing operation, and so the lengths of these two
            lists must match.
    """

    name: str
    timestamp: datetime.datetime
    value: float
    error: Union[Unset, float] = UNSET
    node_ids: Union[Unset, List[int]] = UNSET
    parameter_values: Union[Unset, List[float]] = UNSET

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        name = self.name
        assert self.timestamp.tzinfo is not None, "Datetime must have timezone information"
        timestamp = rfc3339(self.timestamp)

        value = self.value
        error = self.error
        node_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.node_ids, Unset):
            node_ids = self.node_ids

        parameter_values: Union[Unset, List[float]] = UNSET
        if not isinstance(self.parameter_values, Unset):
            parameter_values = self.parameter_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "timestamp": timestamp,
                "value": value,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if node_ids is not UNSET:
            field_dict["node_ids"] = node_ids
        if parameter_values is not UNSET:
            field_dict["parameter_values"] = parameter_values

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        timestamp = isoparse(d.pop("timestamp"))

        value = d.pop("value")

        error = d.pop("error", UNSET)

        node_ids = cast(List[int], d.pop("node_ids", UNSET))

        parameter_values = cast(List[float], d.pop("parameter_values", UNSET))

        characteristic = cls(
            name=name,
            timestamp=timestamp,
            value=value,
            error=error,
            node_ids=node_ids,
            parameter_values=parameter_values,
        )

        return characteristic
