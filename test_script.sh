#!/bin/bash

payloads=(
    '"first_name=Alex&last_name=Doe&phone=+7 999 888 77 66&birth_date=14.10.1999&email=alex.doe@example.com&last_update=2022-03-15&very_last_update=2022-11-27&created_at=2020-01-03"'
    '"field_name_1=email@example.com&field_name_2=+7 111 222 33 44"'
    '"work_email=my_new_super_best_work@domain.com&work_phone=+7 111 222 33 44"'
    '"name=alex&user_email=alex@example.com&password=secret-password&created_at=2023-11-11"'
)

for payload in "${payloads[@]}"; do
    echo '>>>> Request payload:' $payload
    echo '>>>> Received response:'
    curl -X 'POST' \
      'http://127.0.0.1:8000/get_form' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d "$payload"
    echo ''
done


echo 'Sending incorrect payload...'
payload='"first_name=Alex&last_name=Doe&phone=+7 999 888 77 667&birth_date=14.10.1999&email=+7 999 888 77 66&last_update=2022-03-15&very_last_update=2022-11-27&created_at=2020-01-03"'
echo '>>>> Request payload:' $payload
echo 'Received request payload signature:'
curl -X 'POST' \
  'http://127.0.0.1:8000/get_form' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "$payload"
echo ''
