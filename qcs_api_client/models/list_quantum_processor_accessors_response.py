from typing import Any, Callable, Dict, Type, TypeVar, Optional, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union

if TYPE_CHECKING:
    from ..models.quantum_processor_accessor import QuantumProcessorAccessor


T = TypeVar("T", bound="ListQuantumProcessorAccessorsResponse")


@_attrs_define
class ListQuantumProcessorAccessorsResponse:
    """
    Attributes:
        accessors (List['QuantumProcessorAccessor']): Methods of accessing the relevant Quantum Processor
        next_page_token (Union[Unset, str]): Opaque token indicating the start of the next page of results to return; do
            not decode
    """

    accessors: List["QuantumProcessorAccessor"]
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        accessors = []
        for accessors_item_data in self.accessors:
            accessors_item = accessors_item_data.to_dict()
            accessors.append(accessors_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessors": accessors,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quantum_processor_accessor import QuantumProcessorAccessor

        d = src_dict.copy()
        accessors = []
        _accessors = d.pop("accessors")
        for accessors_item_data in _accessors:
            accessors_item = QuantumProcessorAccessor.from_dict(accessors_item_data)

            accessors.append(accessors_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_quantum_processor_accessors_response = cls(
            accessors=accessors,
            next_page_token=next_page_token,
        )

        list_quantum_processor_accessors_response.additional_properties = d
        return list_quantum_processor_accessors_response

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
