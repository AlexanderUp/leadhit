from services import process_request_str


def test_process_request_body():
    request_body = 'f_name1=value1&f_name2=value2'
    processed = process_request_str(request_body)
    expected = {
        'f_name1': 'value1',
        'f_name2': 'value2',
    }
    assert processed == expected
