from typing import Annotated

from fastapi import Body, FastAPI, HTTPException

from domain.domain import process_request
from services import process_request_str
from tiny_database import db

app = FastAPI()


@app.post('/get_form')
async def get_form(body_request: Annotated[str, Body()]):
    try:
        request_dict = process_request_str(body_request)
    except ValueError:
        raise HTTPException(status_code=400)
    templates = db.all()
    return process_request(request_dict, templates)
