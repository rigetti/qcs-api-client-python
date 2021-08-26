from qcs_api_client.models.translate_native_quil_to_encrypted_binary_response_memory_descriptors import (
    TranslateNativeQuilToEncryptedBinaryResponseMemoryDescriptors as MemoryDescriptors,
)


def test_memory_descriptors_additional_properties():
    """"""
    data = {"foo": {"length": 10}}
    memory_descriptors = MemoryDescriptors.from_dict(data)
    assert "foo" in memory_descriptors
    assert memory_descriptors["foo"].length == 10
    assert memory_descriptors.additional_properties["foo"].length == 10

    out = memory_descriptors.to_dict()
    assert "foo" in out
    assert out["foo"]["length"] == 10
