from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StringInput(BaseModel):
    text: str


@app.post("/reverse")
def reverse_string(payload: StringInput):
    return {"reversed": payload.text[::-1]}
