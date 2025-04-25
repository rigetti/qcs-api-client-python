from typing import Any, Callable, Dict, Type, TypeVar, Optional, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union
from ..models.billing_price_object import BillingPriceObject
from ..models.billing_price_scheme import BillingPriceScheme
from ..models.billing_price_price_type import BillingPricePriceType
from ..models.billing_price_tiers_mode import BillingPriceTiersMode

if TYPE_CHECKING:
    from ..models.billing_product import BillingProduct
    from ..models.billing_price_recurrence import BillingPriceRecurrence
    from ..models.tier import Tier


T = TypeVar("T", bound="BillingPrice")


@_attrs_define
class BillingPrice:
    """A configuration for calculating the cost of `BillingProduct` usage
    based on quantity,
    and when that cost should be added as an invoice item.

        Attributes:
            id (str): Unique identifier for the object.
            active (Union[Unset, bool]): Whether the price can be used for new purchases.
            billing_scheme (Union[Unset, BillingPriceScheme]): Use `per_unit` to charge a linear rate per quantity
                (recommended).
                Use `tiered` to charge a dynamic rate based on quantity as defined in the
                `tiers` of a `BillingPice`.
            object_ (Union[Unset, BillingPriceObject]): This object's type, which is always `price`.
            price_type (Union[Unset, BillingPricePriceType]): Use `one_time` to invoice immediately based on a single usage
                report, e.g. purchasing a QPU reservation.
                Use `recurring` to aggregate usage reports over an interval and then invoice
                once based on `BillingPriceRecurrence`, e.g. on-demand QPU usage.
            product (Union[Unset, BillingProduct]): A QCS service product, such as reservation time or on-demand execution.
                One product can be associated with multiple prices, which may be associated
                to particular resources or customers.
            recurring (Union[Unset, BillingPriceRecurrence]): How to invoice for the usage of a product that has a recurring
                (subscription) price.
            tiers (Union[Unset, List['Tier']]): Configure how price should be calculated based on quantity
                when `billingScheme=tiered`.
                Requires at least two tiers.
            tiers_mode (Union[Unset, BillingPriceTiersMode]): Use `graduated` to apply each tier calculation to the portion
                of relevant quantity, e.g. how US federal tax brackets work.
                Use `volume` to apply the highest relevant tier to the entire quantity.
            unit_amount_decimal (Union[Unset, float]): The amount of `currency` to charge per quantity used.
                Requires that `billingScheme=per_unit`.
    """

    id: str
    active: Union[Unset, bool] = UNSET
    billing_scheme: Union[Unset, BillingPriceScheme] = UNSET
    object_: Union[Unset, BillingPriceObject] = UNSET
    price_type: Union[Unset, BillingPricePriceType] = UNSET
    product: Union[Unset, "BillingProduct"] = UNSET
    recurring: Union[Unset, "BillingPriceRecurrence"] = UNSET
    tiers: Union[Unset, List["Tier"]] = UNSET
    tiers_mode: Union[Unset, BillingPriceTiersMode] = UNSET
    unit_amount_decimal: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        id = self.id

        active = self.active

        billing_scheme: Union[Unset, str] = UNSET
        if not isinstance(self.billing_scheme, Unset):
            billing_scheme = self.billing_scheme.value

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

        tiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        tiers_mode: Union[Unset, str] = UNSET
        if not isinstance(self.tiers_mode, Unset):
            tiers_mode = self.tiers_mode.value

        unit_amount_decimal = self.unit_amount_decimal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if billing_scheme is not UNSET:
            field_dict["billingScheme"] = billing_scheme
        if object_ is not UNSET:
            field_dict["object"] = object_
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if product is not UNSET:
            field_dict["product"] = product
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if tiers_mode is not UNSET:
            field_dict["tiersMode"] = tiers_mode
        if unit_amount_decimal is not UNSET:
            field_dict["unitAmountDecimal"] = unit_amount_decimal

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_product import BillingProduct
        from ..models.billing_price_recurrence import BillingPriceRecurrence
        from ..models.tier import Tier

        d = src_dict.copy()
        id = d.pop("id")

        active = d.pop("active", UNSET)

        _billing_scheme = d.pop("billingScheme", UNSET)
        billing_scheme: Union[Unset, BillingPriceScheme]
        if isinstance(_billing_scheme, Unset):
            billing_scheme = UNSET
        else:
            billing_scheme = BillingPriceScheme(_billing_scheme)

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

        tiers = []
        _tiers = d.pop("tiers", UNSET)
        for tiers_item_data in _tiers or []:
            tiers_item = Tier.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        _tiers_mode = d.pop("tiersMode", UNSET)
        tiers_mode: Union[Unset, BillingPriceTiersMode]
        if isinstance(_tiers_mode, Unset):
            tiers_mode = UNSET
        else:
            tiers_mode = BillingPriceTiersMode(_tiers_mode)

        unit_amount_decimal = d.pop("unitAmountDecimal", UNSET)

        billing_price = cls(
            id=id,
            active=active,
            billing_scheme=billing_scheme,
            object_=object_,
            price_type=price_type,
            product=product,
            recurring=recurring,
            tiers=tiers,
            tiers_mode=tiers_mode,
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
