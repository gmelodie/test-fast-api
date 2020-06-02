from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item/{item_name}")
def read_item(item_name: str, query_param: int = 0):
    return {"Item": item_name, "Query": query_param}


# Attributes of Item (the class) come in the request body
@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
