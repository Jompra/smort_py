from smart_home.Weather.collect_combined_forecast import one_call_forecast
from pathlib import Path


def test_one_call_returns_expected_json():
    assert one_call_forecast().status_code == 200
    assert "current" in one_call_forecast().json()


# def test_json_file_is_created():
#   test_json = '{"test_key": "test_value"}'
#   test_file_path = Path('tests/test_weather/dummy_json.json')

#   write_to_file(test_json, test_file_path)

#   assert test_file_path.is_file()

#   test_file_path.unlink()
