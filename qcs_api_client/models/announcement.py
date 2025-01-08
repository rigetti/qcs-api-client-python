from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field
from rfc3339 import rfc3339

from ..types import UNSET
from ..util.serialization import is_not_none


from dateutil.parser import isoparse
import datetime


T = TypeVar("T", bound="Announcement")


@_attrs_define
class Announcement:
    """An announcement to be displayed to users.

    Attributes:
        active (bool): Whether the announcement is currently active.
        content_html (str): The HTML content of the announcement to be displayed.
        created_at (datetime.datetime): The RFC3339-format time the announcement was created.
        id (int):
    """

    active: bool
    content_html: str
    created_at: datetime.datetime
    id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        active = self.active

        content_html = self.content_html

        assert self.created_at.tzinfo is not None, "Datetime must have timezone information"
        created_at = rfc3339(self.created_at)

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "contentHtml": content_html,
                "createdAt": created_at,
                "id": id,
            }
        )

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active")

        content_html = d.pop("contentHtml")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        announcement = cls(
            active=active,
            content_html=content_html,
            created_at=created_at,
            id=id,
        )

        announcement.additional_properties = d
        return announcement

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
