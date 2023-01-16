from .main import app

items = [{"foo": "The Foo Wrestlers"}, {"bar": "The Bar Fighters"}, {"baz": "The Baz Fighters"}]

@app.get("/items")
async def read_items(items: list = items):
    return {"message": items}