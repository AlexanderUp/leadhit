import pytest

from domain.domain import (
    FIELD_VALIDATION_FUNCTION_DICT,
    FieldType,
    get_field_type,
    get_request_signature,
    process_request,
)
from fixtures.data import FAKE_DATABASE


@pytest.mark.parametrize(
    ('field_value', 'expected_type'),
    [
        ('14.10.1999', FieldType.DATE),
        ('2022-03-15', FieldType.DATE),
        ('+7 999 888 77 66', FieldType.PHONE),
        ('alex.doe@example.com', FieldType.EMAIL),
        ('random_text', FieldType.TEXT),
    ],
)
def test_get_field_type(field_value, expected_type):
    field_type = get_field_type(field_value, FIELD_VALIDATION_FUNCTION_DICT)
    assert field_type == expected_type


def test_request_signature():
    request = {
        'first_name': 'Alex',
        'last_name': 'Doe',
        'phone': '+7 999 888 77 66',
        'birth_date': '14.10.1999',
        'email': 'alex.doe@example.com',
        'last_update': '2022-03-15',
        'very_last_update': '2022-11-27',
        'created_at': '2020-01-03',
    }
    expected = {
        'first_name': 'text',
        'last_name': 'text',
        'phone': 'phone',
        'birth_date': 'date',
        'email': 'email',
        'last_update': 'date',
        'very_last_update': 'date',
        'created_at': 'date',
    }
    request_signature = get_request_signature(request)
    assert request_signature == expected


def test_correct_request():
    fake_request = {
        'first_name': 'Alex',
        'last_name': 'Doe',
        'phone': '+7 999 888 77 66',
        'birth_date': '14.10.1999',
        'email': 'alex.doe@example.com',
        'last_update': '2022-03-15',
        'very_last_update': '2022-11-27',
        'created_at': '2020-01-03',
    }
    request_result = process_request(fake_request, FAKE_DATABASE)
    assert request_result == 'Person'


def test_request_field_missing():
    wrong_fake_request = {
        'first_name': 'Alex',
        'last_name': 'Doe',
        'birth_date': '14.10.1999',
        'email': 'alex.doe@example.com',
        'last_update': '2022-03-15',
        'very_last_update': '2022-11-27',
        'created_at': '2020-01-03',
    }
    expected = {
        'first_name': 'text',
        'last_name': 'text',
        'birth_date': 'date',
        'email': 'email',
        'last_update': 'date',
        'very_last_update': 'date',
        'created_at': 'date',
    }
    request_result = process_request(wrong_fake_request, FAKE_DATABASE)
    assert request_result == expected


def test_request_field_type_incorrect():
    invalid_fake_request = {
        'first_name': 'Alex',
        'last_name': 'Doe',
        'phone': '+7 999 888 77 66',
        'birth_date': '14.10.1999',
        'email': '+7 999 888 77 66',
        'last_update': '2022-03-15',
        'very_last_update': '2022-11-27',
        'created_at': '2020-01-03',
    }
    expected = {
        'first_name': 'text',
        'last_name': 'text',
        'phone': 'phone',
        'birth_date': 'date',
        'email': 'phone',
        'last_update': 'date',
        'very_last_update': 'date',
        'created_at': 'date',
    }
    request_result = process_request(invalid_fake_request, FAKE_DATABASE)
    assert request_result == expected
