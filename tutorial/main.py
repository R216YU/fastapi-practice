from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    ryu = "ryu"
    kaz = "kaz"
    

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.ryu:
        return {"model_name": model_name, "message": "R216YU"}

    if model_name.value == "kaz":
        return {"model_name": model_name, "message": "K114Z"}

    return {"model_name": model_name, "message": "Others"}