from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union
from ..models.product import Product


T = TypeVar("T", bound="GetAccountEventBillingPriceRequest")


@_attrs_define
class GetAccountEventBillingPriceRequest:
    """Property `quantumProcessorId` is currently required for all `product`s, however in the future there may be
    `product`s that do not require a `quantumProcessorId`.

        Attributes:
            product (Product): The set of known QCS service products.
            quantum_processor_id (Union[Unset, str]):
    """

    product: Product
    quantum_processor_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        product = self.product.value

        quantum_processor_id = self.quantum_processor_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
            }
        )
        if quantum_processor_id is not UNSET:
            field_dict["quantumProcessorId"] = quantum_processor_id

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product = Product(d.pop("product"))

        quantum_processor_id = d.pop("quantumProcessorId", UNSET)

        get_account_event_billing_price_request = cls(
            product=product,
            quantum_processor_id=quantum_processor_id,
        )

        get_account_event_billing_price_request.additional_properties = d
        return get_account_event_billing_price_request

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
