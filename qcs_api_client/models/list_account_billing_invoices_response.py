from typing import Any, Callable, Dict, Type, TypeVar, Optional, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none


from typing import Union

if TYPE_CHECKING:
    from ..models.billing_invoice import BillingInvoice


T = TypeVar("T", bound="ListAccountBillingInvoicesResponse")


@_attrs_define
class ListAccountBillingInvoicesResponse:
    """
    Attributes:
        billing_invoices (List['BillingInvoice']):
        next_page_token (Union[Unset, str]):
    """

    billing_invoices: List["BillingInvoice"]
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        billing_invoices = []
        for billing_invoices_item_data in self.billing_invoices:
            billing_invoices_item = billing_invoices_item_data.to_dict()
            billing_invoices.append(billing_invoices_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingInvoices": billing_invoices,
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
        from ..models.billing_invoice import BillingInvoice

        d = src_dict.copy()
        billing_invoices = []
        _billing_invoices = d.pop("billingInvoices")
        for billing_invoices_item_data in _billing_invoices:
            billing_invoices_item = BillingInvoice.from_dict(billing_invoices_item_data)

            billing_invoices.append(billing_invoices_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_account_billing_invoices_response = cls(
            billing_invoices=billing_invoices,
            next_page_token=next_page_token,
        )

        list_account_billing_invoices_response.additional_properties = d
        return list_account_billing_invoices_response

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
