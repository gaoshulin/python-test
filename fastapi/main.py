from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# 定义 子模型
class Image(BaseModel):
    url: str
    name: str


# 嵌套模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    # 子模型
    image: Image | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = Query(default=None, min_length=3, max_length=30)):
    # item_id: 必须参数，类型为 int    
    # q: 可选参数，验证参数长度  min_length=3, max_length=30
    return {"item_id": item_id, "q": q}


# 请求体
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "price": item.price}


# 响应体
@app.post("/items")
async def create_item(item: Item):
    return item


# 启动命令
# uvicorn main:app --reload

