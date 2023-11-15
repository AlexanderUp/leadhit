import pytest

from domain.domain_aux_utils import is_date, is_email, is_phone


@pytest.mark.parametrize('date', ['14.11.2023', '2023-11-14'])
def test_date_validation(date):
    assert is_date(date)


def test_phone_validation_success():
    assert is_phone('+7 999 999 99 99')


@pytest.mark.parametrize(
    'phone_number',
    [
        '+7 999 999 99 9999',
        '+7 9999999999',
        '+79999999999',
        '+19999999999',
        '#19999999999',
        '19999999999',
    ],
)
def test_phone_validation_failure(phone_number):
    assert not is_phone(phone_number)


def test_email_validation():
    assert is_email('admin@example.com')


@pytest.mark.parametrize(
    'email',
    [
        'admin@example.com.com',
        'admin@example',
        '@example.com',
        'example.com',
        '@admin@example.com',
        '##admin@example.com',
    ],
)
def test_email_validation_failure(email):
    assert not is_email(email)
