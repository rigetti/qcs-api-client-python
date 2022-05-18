import datetime
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..models.user_profile import UserProfile
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        created_time (datetime.datetime):
        id (int):
        idp_id (str):
        profile (Union[Unset, UserProfile]):
    """

    created_time: datetime.datetime
    id: int
    idp_id: str
    profile: Union[Unset, UserProfile] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        assert self.created_time.tzinfo is not None, "Datetime must have timezone information"
        created_time = rfc3339(self.created_time)

        id = self.id
        idp_id = self.idp_id
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdTime": created_time,
                "id": id,
                "idpId": idp_id,
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_time = isoparse(d.pop("createdTime"))

        id = d.pop("id")

        idp_id = d.pop("idpId")

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, UserProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = UserProfile.from_dict(_profile)

        user = cls(
            created_time=created_time,
            id=id,
            idp_id=idp_id,
            profile=profile,
        )

        user.additional_properties = d
        return user

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
