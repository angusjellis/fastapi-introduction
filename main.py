from enum import Enum

from fastapi import FastAPI

# These are all machine learning models.
# This class is inherited from the Enum class.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}

items = [{"foo": "The Foo Wrestlers"}, {"bar": "The Bar Fighters"}, {"baz": "The Baz Fighters"}]

@app.get("/items")
# API endpoints get documented automatically.
async def read_items(items: list = items):
    return {"message": items}

@app.get("/items/{item_id}")
# type hints automatically convert the path parameter to the correct type.
# if you pass in a stringified number (such as "3"), it will convert it to an int.
# if you pass in a string that cannot be converted (such as "three"), it will raise a 422 error.
async def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/models/{model_name}")
# This route will only be called if the model_name parameter is one of the choices in the ModelName enum.
# If it is not, it will raise a 422 error.
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}