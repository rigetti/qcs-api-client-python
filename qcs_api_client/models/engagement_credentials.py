from typing import Any, Callable, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..util.serialization import is_not_none


T = TypeVar("T", bound="EngagementCredentials")


@_attrs_define
class EngagementCredentials:
    """Credentials are the ZeroMQ CURVE Keys used to encrypt the connection with the Quantum Processor
    Endpoint.

        Attributes:
            client_public (str):
            client_secret (str):
            server_public (str):
    """

    client_public: str
    client_secret: str
    server_public: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        client_public = self.client_public

        client_secret = self.client_secret

        server_public = self.server_public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientPublic": client_public,
                "clientSecret": client_secret,
                "serverPublic": server_public,
            }
        )

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_public = d.pop("clientPublic")

        client_secret = d.pop("clientSecret")

        server_public = d.pop("serverPublic")

        engagement_credentials = cls(
            client_public=client_public,
            client_secret=client_secret,
            server_public=server_public,
        )

        engagement_credentials.additional_properties = d
        return engagement_credentials

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
