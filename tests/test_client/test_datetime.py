from qcs_api_client.models import Characteristic
from datetime import datetime
from dateutil.tz import tzutc


def test_sync_client_api_call():
    """"""
    data = {
        "name": "MEASURE",
        "timestamp": "2021-03-09T01:29:30Z",
        "value": 0.1,
    }
    expected_datetime = datetime(2021, 3, 9, 1, 29, 30, tzinfo=tzutc())
    characteristic = Characteristic.from_dict(data)
    assert characteristic.timestamp == expected_datetime

    out = characteristic.to_dict()
    assert out["timestamp"] == "2021-03-09T01:29:30+00:00"
    assert "error" not in out
    assert "node_ids" not in out
    assert "parameter_values" not in out
