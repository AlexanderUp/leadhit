def process_request_str(request_str: str) -> dict[str, str]:
    pair_strings = request_str.strip().split('&')
    data_pairs = [pair.split('=') for pair in pair_strings]
    request_dict = {key: field_value for key, field_value in data_pairs}
    return request_dict
