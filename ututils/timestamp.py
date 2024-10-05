from datetime import datetime, date


def to_yyyymmdd_str(datetime_obj: datetime | date) -> str:
    """
    Returns yyyymmdd string representation of datetime/date object.

    :param datetime_obj: datetime/date object to convert
    :return: date as a yyyymmdd string
    """
    return datetime_obj.strftime('%Y%m%d')


def from_yyyymmdd_str(yyyymmdd_str: str) -> datetime:
    """
    Returns a datetime object constructed from a date represented as 8 character string: yyyymmdd.

    :param yyyymmdd_str: string like 20120811
    :return: a datetime object
    """
    # strptime is very forgiving with it's parsing, so dates like 202451 will get parsed to 1st May, 2024. We don't
    # want this, so we just add a simple length check here.
    if len(yyyymmdd_str) != 8:
        raise ValueError(
            f"Input string ({yyyymmdd_str}) must be 8 characters long. Got {len(yyyymmdd_str)} characters instead.")

    try:
        return datetime.strptime(yyyymmdd_str, '%Y%m%d')
    except ValueError as e:
        # strptime is forgiving as a parser, so when it tries to convert sometime like 2024941, it assumes year =
        # 2024, month = 09 and day = 04, and then throws an error like "unconverted data remains: 1". So instead we
        # do our own errors.
        month = int(yyyymmdd_str[4:6])
        if month < 1 or month > 12:
            raise ValueError(f"Month expected to be between 01 and 12, got {month} instead.")

        day = int(yyyymmdd_str[6:])
        if day < 1 or day > 31:
            raise ValueError(f"Day expected to be between 01 and 31, got {day} instead.")

        raise e
