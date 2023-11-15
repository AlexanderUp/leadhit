FAKE_DATABASE: list[dict[str, str]] = [
    {
        'name': 'Form template name',
        'field_name_1': 'email',
        'field_name_2': 'phone',
    },
    {
        'name': 'Person',
        'first_name': 'text',
        'last_name': 'text',
        'phone': 'phone',
        'birth_date': 'date',
        'email': 'email',
        'last_update': 'date',
    },
    {
        'name': 'Work',
        'work_email': 'email',
        'work_phone': 'phone',
    },
    {
        'name': 'User',
        'user_email': 'email',
        'password': 'text',
        'created_at': 'date',
    },
    {
        'name': 'Next of kin',
        'kin_full_name': 'text',
        'kin_email': 'email',
        'kin_phone': 'phone',
        'kin_adress': 'text',
    },
]
