from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union


T = TypeVar("T", bound="QuantumProcessorCalendar")


@_attrs_define
class QuantumProcessorCalendar:
    """Details about calendars related to a quantum processor.

    Attributes:
        maintenance_i_cal (Union[Unset, str]): This calendar's schedule contains maintenance events for the QPU, during
            which execution is not available.
    """

    maintenance_i_cal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        maintenance_i_cal = self.maintenance_i_cal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_i_cal is not UNSET:
            field_dict["maintenanceICal"] = maintenance_i_cal

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        maintenance_i_cal = d.pop("maintenanceICal", UNSET)

        quantum_processor_calendar = cls(
            maintenance_i_cal=maintenance_i_cal,
        )

        quantum_processor_calendar.additional_properties = d
        return quantum_processor_calendar

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
