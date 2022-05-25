from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.billing_price_object import BillingPriceObject
from ..models.billing_price_price_type import BillingPricePriceType
from ..models.billing_price_recurrence import BillingPriceRecurrence
from ..models.billing_product import BillingProduct
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="BillingPrice")


@attr.s(auto_attribs=True)
class BillingPrice:
    """The price schedule for a particular service applied to an invoice line item.

    Attributes:
        id (str): Unique identifier for the object.
        object_ (Union[Unset, BillingPriceObject]): String representing the object's type. Objects of the same type
            share the same value.
        price_type (Union[Unset, BillingPricePriceType]): One of `one_time` or `recurring` depending on whether the
            price is for a one-time purchase or a recurring (subscription) purchase.
        product (Union[Unset, BillingProduct]): A QCS service product. This may represent one time (such as
            reservations) or metered services.
        recurring (Union[Unset, BillingPriceRecurrence]): The recurring components of a price such as `interval` and
            `usageType`.
        unit_amount_decimal (Union[Unset, str]): The unit amount in `currency` to be charged, represented as a decimal
            string with at most 12 decimal places. Only set if `billingScheme=per_unit`.
    """

    id: str
    object_: Union[Unset, BillingPriceObject] = UNSET
    price_type: Union[Unset, BillingPricePriceType] = UNSET
    product: Union[Unset, BillingProduct] = UNSET
    recurring: Union[Unset, BillingPriceRecurrence] = UNSET
    unit_amount_decimal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        id = self.id
        object_: Union[Unset, str] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        recurring: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurring, Unset):
            recurring = self.recurring.to_dict()

        unit_amount_decimal = self.unit_amount_decimal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if product is not UNSET:
            field_dict["product"] = product
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if unit_amount_decimal is not UNSET:
            field_dict["unitAmountDecimal"] = unit_amount_decimal

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, BillingPriceObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = BillingPriceObject(_object_)

        _price_type = d.pop("priceType", UNSET)
        price_type: Union[Unset, BillingPricePriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = BillingPricePriceType(_price_type)

        _product = d.pop("product", UNSET)
        product: Union[Unset, BillingProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = BillingProduct.from_dict(_product)

        _recurring = d.pop("recurring", UNSET)
        recurring: Union[Unset, BillingPriceRecurrence]
        if isinstance(_recurring, Unset):
            recurring = UNSET
        else:
            recurring = BillingPriceRecurrence.from_dict(_recurring)

        unit_amount_decimal = d.pop("unitAmountDecimal", UNSET)

        billing_price = cls(
            id=id,
            object_=object_,
            price_type=price_type,
            product=product,
            recurring=recurring,
            unit_amount_decimal=unit_amount_decimal,
        )

        billing_price.additional_properties = d
        return billing_price

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
