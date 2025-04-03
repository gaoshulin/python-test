from typing import Union
from typing import Annotated
from fastapi import FastAPI, Query, Depends, Header, Cookie, UploadFile
from pydantic import BaseModel
from fastapi import HTTPException
from users import router

# 依赖注入
async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# 依赖注入
async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# 全局依赖注入
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
app.include_router(router, tags=["users"])


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


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
def read_item(item_id: int, 
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
    q: Union[str, None] = Query(default=None, min_length=3, max_length=30)
 ):
    # item_id: 必须参数，类型为 int    
    # q: 可选参数，验证参数长度  min_length=3, max_length=30
    return {"item_id": item_id, "ads_id": ads_id, "user_agent": user_agent, "q": q}


# 请求体
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "price": item.price}


# 响应体
@app.post("/items")
async def create_item(item: Item):
    return item


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        # return {"message": "No upload file sent"}
        # 错误异常处理
        raise HTTPException(status_code=404, detail="No upload file sent")
    else:
        return {"filename": file.filename}


# 启动命令
# uvicorn main:app --reload
