from enum import Enum
from typing import Callable

from domain.domain_aux_utils import is_date, is_email, is_phone
from fixtures.data import FAKE_DATABASE


class FieldType(Enum):
    DATE = 'date'
    PHONE = 'phone'
    EMAIL = 'email'
    TEXT = 'text'


FIELD_VALIDATION_FUNCTION_DICT: dict[Callable, FieldType] = {
    is_date: FieldType.DATE,
    is_email: FieldType.EMAIL,
    is_phone: FieldType.PHONE,
}


def get_field_type(
    field_value: str,
    field_functions: dict[Callable, FieldType] = FIELD_VALIDATION_FUNCTION_DICT,
) -> FieldType:
    for func in field_functions:
        if func(field_value):
            return field_functions[func]
    return FieldType.TEXT


def get_request_signature(requst_dict: dict[str, str]) -> dict[str, str]:
    return {
        key: get_field_type(field_value).value
        for key, field_value in requst_dict.items()
    }


def get_template_name(
    request_signature: dict[str, str],
    all_templates: list[dict[str, str]],
) -> str | None:
    template_name = None

    for template in all_templates:
        template_fields_set = set(template)
        template_fields_set.remove('name')

        if template_fields_set.issubset(set(request_signature)):
            for template_key in template_fields_set:
                if template[template_key] != request_signature[template_key]:
                    break
            else:
                template_name = template['name']
    return template_name


def process_request(
    request: dict[str, str],
    all_templates: list[dict[str, str]],
) -> str | dict[str, str]:
    request_signature = get_request_signature(request)
    template_name = get_template_name(request_signature, all_templates)
    if not template_name:
        return request_signature
    return template_name


if __name__ == '__main__':
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

    # phone field missing
    wrong_fake_request = {
        'first_name': 'Alex',
        'last_name': 'Doe',
        'birth_date': '14.10.1999',
        'email': 'alex.doe@example.com',
        'last_update': '2022-03-15',
        'very_last_update': '2022-11-27',
        'created_at': '2020-01-03',
    }

    # email field incorrect type
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

    print(process_request(fake_request, FAKE_DATABASE))
    print(process_request(wrong_fake_request, FAKE_DATABASE))
    print(process_request(invalid_fake_request, FAKE_DATABASE))
