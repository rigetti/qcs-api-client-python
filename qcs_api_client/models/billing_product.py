from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union
from ..models.billing_product_object import BillingProductObject


T = TypeVar("T", bound="BillingProduct")


@_attrs_define
class BillingProduct:
    """A QCS service product, such as reservation time or on-demand execution.
    One product can be associated with multiple prices, which may be associated
    to particular resources or customers.

        Attributes:
            id (str): Unique identifier for the object.
            name (str): This name will show up on associated invoice line item descriptions.
            object_ (BillingProductObject): This object's type, which is always `product`.
            description (Union[Unset, str]):
            unit_label (Union[Unset, str]): A label for units of this product which appears on customer
                invoices, e.g. "microseconds" for on-demand execution or "minutes" for
                qpu reservations.
    """

    id: str
    name: str
    object_: BillingProductObject
    description: Union[Unset, str] = UNSET
    unit_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        id = self.id

        name = self.name

        object_ = self.object_.value

        description = self.description

        unit_label = self.unit_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "object": object_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unit_label is not UNSET:
            field_dict["unitLabel"] = unit_label

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        object_ = BillingProductObject(d.pop("object"))

        description = d.pop("description", UNSET)

        unit_label = d.pop("unitLabel", UNSET)

        billing_product = cls(
            id=id,
            name=name,
            object_=object_,
            description=description,
            unit_label=unit_label,
        )

        billing_product.additional_properties = d
        return billing_product

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
