import datetime
import re


def is_date_dotted(string_value: str) -> bool:
    try:
        datetime.datetime.strptime(string_value, '%d.%m.%Y')
    except ValueError:
        return False
    return True


def is_date_dashed(string_value: str) -> bool:
    try:
        datetime.datetime.strptime(string_value, '%Y-%m-%d')
    except ValueError:
        return False
    return True


def is_date(string_value: str) -> bool:
    if any((is_date_dotted(string_value), is_date_dashed(string_value))):
        return True
    return False


def is_phone(string_value: str) -> bool:
    pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    if re.match(pattern, string_value):
        return True
    return False


def is_email(string_value: str) -> bool:
    pattern = re.compile(r'^\w+[\w\.-]+@[\w-]+\.+[a-z]{2,4}$')
    if re.match(pattern, string_value):
        return True
    return False
