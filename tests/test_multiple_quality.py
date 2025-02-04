import nemreader as nr
import pytest


def test_correct_records():
    meter_data = nr.read_nem_file(
        "examples/unzipped/Example_NEM12_multiple_quality.csv"
    )
    readings = meter_data.readings["CCCC123456"]["E1"]
    assert len(readings) == 48
    assert readings[0].read_value == pytest.approx(18.023, 0.1)
    assert readings[-1].read_value == pytest.approx(14.733, 0.1)


def test_correct_quality():
    meter_data = nr.read_nem_file(
        "examples/unzipped/Example_NEM12_multiple_quality.csv"
    )
    readings = meter_data.readings["CCCC123456"]["E1"]
    assert readings[0].quality_method == "F14"
    assert readings[10].quality_method == "F14"
    assert readings[19].quality_method == "F14"
    assert readings[20].quality_method == "A"
    assert readings[22].quality_method == "A"
    assert readings[23].quality_method == "A"
    assert readings[25].quality_method == "S14"
    assert readings[30].quality_method == "S14"
    assert readings[47].quality_method == "S14"
