from datetime import datetime, date

import pytest

from ututils.timestamp import to_yyyymmdd_str, from_yyyymmdd_str


def test_to_yyyymmdd_str_from_basic_datetime():
    datetime_obj = datetime(year=2024, month=10, day=12)

    assert to_yyyymmdd_str(datetime_obj) == '20241012'


def test_to_yyyymmdd_str_from_object_containing_time_returns_only_date():
    datetime_obj = datetime(year=2024, month=10, day=12, hour=12, minute=59, second=30)

    assert to_yyyymmdd_str(datetime_obj) == '20241012'


def test_to_yyyymmdd_str_from_date_obj():
    datetime_obj = date(year=2024, month=10, day=12)

    assert to_yyyymmdd_str(datetime_obj) == '20241012'


def test_to_yyyymmdd_str_from_date_with_single_digit():
    datetime_obj = date(year=2024, month=5, day=7)

    assert to_yyyymmdd_str(datetime_obj) == '20240507'


def test_from_yyyymmdd_str_from_basic_date_str():
    date_str = '20241012'

    returned_datetime_obj = from_yyyymmdd_str(date_str)

    # check variables instead of whole object because we don't care about time values
    assert returned_datetime_obj.year == 2024
    assert returned_datetime_obj.month == 10
    assert returned_datetime_obj.day == 12


def test_from_yyyymmdd_str_from_too_long_date_str_raises_value_error():
    date_str = '202410125'

    with pytest.raises(ValueError):
        from_yyyymmdd_str(date_str)


def test_from_yyyymmdd_str_from_too_short_date_str_raises_value_error():
    date_str = '20251'

    with pytest.raises(ValueError):
        from_yyyymmdd_str(date_str)


def test_from_yyyymmdd_str_date_with_invalid_month_raises_value_error():
    date_str = '20242301'

    with pytest.raises(ValueError):
        from_yyyymmdd_str(date_str)


def test_from_yyyymmdd_str_date_with_invalid_day_raises_value_error():
    date_str = '20241199'

    with pytest.raises(ValueError):
        from_yyyymmdd_str(date_str)


def test_from_yyyymmdd_str_returns_datetime_object():
    date_str = '20241012'

    assert isinstance(from_yyyymmdd_str(date_str),
                      datetime) is True, f"Expected return type of function to be datetime object."
