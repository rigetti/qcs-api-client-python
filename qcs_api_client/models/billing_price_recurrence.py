from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from ..models.billing_price_recurrence_usage_type import BillingPriceRecurrenceUsageType
from ..models.billing_price_recurrence_aggregate_usage import (
    BillingPriceRecurrenceAggregateUsage,
)
from typing import Union
from ..models.billing_price_recurrence_interval import BillingPriceRecurrenceInterval


T = TypeVar("T", bound="BillingPriceRecurrence")


@_attrs_define
class BillingPriceRecurrence:
    """How to invoice for the usage of a product that has a recurring
    (subscription) price.

        Attributes:
            interval (BillingPriceRecurrenceInterval): The frequency at which recurring usage should be billed.
                Using `month` is recommended.
            aggregate_usage (Union[Unset, BillingPriceRecurrenceAggregateUsage]): How to determine the aggregate usage over
                the `interval` when
                `usageType=metered`.
                Using `sum` is recommended.
            interval_count (Union[Unset, int]): The number of `interval` units between each billing cycle.
                For example, `interval=month` and `intervalCount=1` means every month
                (recommended).
            usage_type (Union[Unset, BillingPriceRecurrenceUsageType]): Use `metered` to calculate a dynamic quantity based
                on reported
                usage records (recommended).
                Use `licensed` when you provide a fixed quantity, e.g. a TV subscription.
    """

    interval: BillingPriceRecurrenceInterval
    aggregate_usage: Union[Unset, BillingPriceRecurrenceAggregateUsage] = UNSET
    interval_count: Union[Unset, int] = UNSET
    usage_type: Union[Unset, BillingPriceRecurrenceUsageType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        interval = self.interval.value

        aggregate_usage: Union[Unset, str] = UNSET
        if not isinstance(self.aggregate_usage, Unset):
            aggregate_usage = self.aggregate_usage.value

        interval_count = self.interval_count

        usage_type: Union[Unset, str] = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
            }
        )
        if aggregate_usage is not UNSET:
            field_dict["aggregateUsage"] = aggregate_usage
        if interval_count is not UNSET:
            field_dict["intervalCount"] = interval_count
        if usage_type is not UNSET:
            field_dict["usageType"] = usage_type

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = BillingPriceRecurrenceInterval(d.pop("interval"))

        _aggregate_usage = d.pop("aggregateUsage", UNSET)
        aggregate_usage: Union[Unset, BillingPriceRecurrenceAggregateUsage]
        if isinstance(_aggregate_usage, Unset):
            aggregate_usage = UNSET
        else:
            aggregate_usage = BillingPriceRecurrenceAggregateUsage(_aggregate_usage)

        interval_count = d.pop("intervalCount", UNSET)

        _usage_type = d.pop("usageType", UNSET)
        usage_type: Union[Unset, BillingPriceRecurrenceUsageType]
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = BillingPriceRecurrenceUsageType(_usage_type)

        billing_price_recurrence = cls(
            interval=interval,
            aggregate_usage=aggregate_usage,
            interval_count=interval_count,
            usage_type=usage_type,
        )

        billing_price_recurrence.additional_properties = d
        return billing_price_recurrence

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
