from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.nomad_job_datacenters import NomadJobDatacenters
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="CreateEndpointParameters")


@attr.s(auto_attribs=True)
class CreateEndpointParameters:
    """A publicly available set of parameters for defining an endpoint.

    Attributes:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]
        datacenters (Union[Unset, List[NomadJobDatacenters]]): Which datacenters are available for endpoint placement.
            Defaults to berkeley-775
    """

    quantum_processor_id: str
    datacenters: Union[Unset, List[NomadJobDatacenters]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Optional[Callable[[Any], bool]] = is_not_none) -> Dict[str, Any]:
        quantum_processor_id = self.quantum_processor_id
        datacenters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.datacenters, Unset):
            datacenters = []
            for datacenters_item_data in self.datacenters:
                datacenters_item = datacenters_item_data.value

                datacenters.append(datacenters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantumProcessorId": quantum_processor_id,
            }
        )
        if datacenters is not UNSET:
            field_dict["datacenters"] = datacenters

        field_dict = {k: v for k, v in field_dict.items() if v != UNSET}
        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantum_processor_id = d.pop("quantumProcessorId")

        datacenters = []
        _datacenters = d.pop("datacenters", UNSET)
        for datacenters_item_data in _datacenters or []:
            datacenters_item = NomadJobDatacenters(datacenters_item_data)

            datacenters.append(datacenters_item)

        create_endpoint_parameters = cls(
            quantum_processor_id=quantum_processor_id,
            datacenters=datacenters,
        )

        create_endpoint_parameters.additional_properties = d
        return create_endpoint_parameters

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
