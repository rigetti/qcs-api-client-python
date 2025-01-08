from typing import Any, Callable, Dict, Type, TypeVar, Optional, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union

if TYPE_CHECKING:
    from ..models.instruction_set_architecture import InstructionSetArchitecture


T = TypeVar("T", bound="ListInstructionSetArchitectureResponse")


@_attrs_define
class ListInstructionSetArchitectureResponse:
    """
    Attributes:
        instruction_set_architectures (List['InstructionSetArchitecture']):
        next_page_token (Union[Unset, str]): Send an opaque page token returned from a prior request
    """

    instruction_set_architectures: List["InstructionSetArchitecture"]
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        instruction_set_architectures = []
        for instruction_set_architectures_item_data in self.instruction_set_architectures:
            instruction_set_architectures_item = instruction_set_architectures_item_data.to_dict()
            instruction_set_architectures.append(instruction_set_architectures_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructionSetArchitectures": instruction_set_architectures,
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
        from ..models.instruction_set_architecture import InstructionSetArchitecture

        d = src_dict.copy()
        instruction_set_architectures = []
        _instruction_set_architectures = d.pop("instructionSetArchitectures")
        for instruction_set_architectures_item_data in _instruction_set_architectures:
            instruction_set_architectures_item = InstructionSetArchitecture.from_dict(
                instruction_set_architectures_item_data
            )

            instruction_set_architectures.append(instruction_set_architectures_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_instruction_set_architecture_response = cls(
            instruction_set_architectures=instruction_set_architectures,
            next_page_token=next_page_token,
        )

        list_instruction_set_architecture_response.additional_properties = d
        return list_instruction_set_architecture_response

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
