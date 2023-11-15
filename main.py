from typing import Annotated

from fastapi import Body, FastAPI, HTTPException

from domain.domain import process_request
from fixtures.data import FAKE_DATABASE
from services import process_request_str

app = FastAPI()


@app.post('/get_form')
async def get_form(body_request: Annotated[str, Body()]):
    try:
        request_dict = process_request_str(body_request)
    except ValueError:
        raise HTTPException(status_code=400)
    return process_request(request_dict, FAKE_DATABASE)
