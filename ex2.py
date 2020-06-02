
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# FastAPI escapes chars and uses utf-8
# Try http://localhost:8000/item/á`~ção
@app.get("/item/{item_name}")
def read_item(item_name: str):
    return {"Item": item_name}
