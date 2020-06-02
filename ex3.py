from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# You can query send query parameters as well
# Try http://localhost:8000/item/hi?query_param=blabla
@app.get("/item/{item_name}")
def read_item(item_name: str, query_param: int = 0):
    return {"Item": item_name, "Query": query_param}
