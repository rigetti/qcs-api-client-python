from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union
from ..models.product import Product


T = TypeVar("T", bound="EventBillingPriceRate")


@_attrs_define
class EventBillingPriceRate:
    """The per-unit price associated with a particular QCS service product,
    and (optionally) with a particular quantum processor.

        Attributes:
            id (int):
            product (Product): The set of known QCS service products.
            quantum_processor_id (Union[Unset, str]): If unset, this per-unit price applies to any quantum processor.
            unit_amount_decimal (Union[Unset, float]): The unit amount in currency to be charged.
            unit_label (Union[Unset, str]): Human-readable unit label infomation.
    """

    id: int
    product: Product
    quantum_processor_id: Union[Unset, str] = UNSET
    unit_amount_decimal: Union[Unset, float] = UNSET
    unit_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        id = self.id

        product = self.product.value

        quantum_processor_id = self.quantum_processor_id

        unit_amount_decimal = self.unit_amount_decimal

        unit_label = self.unit_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product": product,
            }
        )
        if quantum_processor_id is not UNSET:
            field_dict["quantumProcessorId"] = quantum_processor_id
        if unit_amount_decimal is not UNSET:
            field_dict["unitAmountDecimal"] = unit_amount_decimal
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

        product = Product(d.pop("product"))

        quantum_processor_id = d.pop("quantumProcessorId", UNSET)

        unit_amount_decimal = d.pop("unitAmountDecimal", UNSET)

        unit_label = d.pop("unitLabel", UNSET)

        event_billing_price_rate = cls(
            id=id,
            product=product,
            quantum_processor_id=quantum_processor_id,
            unit_amount_decimal=unit_amount_decimal,
            unit_label=unit_label,
        )

        event_billing_price_rate.additional_properties = d
        return event_billing_price_rate

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
