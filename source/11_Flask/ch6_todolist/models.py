# pip install pydantic
from pydantic import BaseModel
from typing import Optional  # 🔥 이게 없어서 NameError 발생
class TodoRequest(BaseModel):
    id : int
    content : str
    # is_done : bool | None=False
    is_done: Optional[bool] = False  # ✅ Optional 사용

if __name__ == '__main__':
    todo = TodoRequest(id='1', content='flask 공부', is_done="True")
    # print(todo.dict()) # todo 객체를 dict 형태로 변환
    print(todo.model_dump()) # todo 객체를 dict 형태로 변환

