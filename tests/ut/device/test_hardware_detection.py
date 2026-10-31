import importlib.util
from pathlib import Path

_HARDWARE_PATH = Path(__file__).parents[3] / "vllm_ascend" / "device" / "hardware.py"
_SPEC = importlib.util.spec_from_file_location("ascend_hardware_detection", _HARDWARE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
hardware = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(hardware)


def test_legacy_ascend_310_is_distinguished_from_310p() -> None:
    assert hardware.is_legacy_ascend310("310")
    assert not hardware.is_legacy_ascend310("310P1")


def test_310p_detection_keeps_the_existing_soc_name() -> None:
    assert not hardware.is_legacy_ascend310("Ascend310P1")
