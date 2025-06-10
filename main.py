from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

from models import Base
from database import engine
from routers.auth import router as auth_router
from routers.todo import router as todo_router
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

app.include_router(auth_router)
app.include_router(todo_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root(request: Request):
    #request. ile kullanıcı tarafından gelen her türlü isteklere erişebiliyoruz
    return RedirectResponse(url="/todo/todo-page")  #Burada kullanıcı bildirim gönderince nereye attığını gösteriyor




#main dosyasını böldük
"""from fastapi import FastAPI, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from models import Todo
from models import Base
from database import engine, SessionLocal
from typing import Annotated
from pydantic import BaseModel,Field
from routers.auth import router as auth_router


app=FastAPI()
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

#İstenilen ölçeklerde ekleme yapılsın diye
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=1000)
    priority: int = Field(gt=0, lt=6)
    complete: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/read_all")
async def read_all(db: db_dependency):
    return db.query(Todo).all()
#databasedeki tüm verilere ulaşır

@app.get(path="/get_by_id/{todo_id}", status_code=status.HTTP_200_OK)
async def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

#databasede id ile aratır ve veriyi getirir.



@app.post(path="/create_todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo = Todo(**todo_request.dict())
    db.add(todo)
    db.commit()

#Veri Ekleme


@app.put(path="/update_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency,
    todo_request: TodoRequest,
    todo_id: int = Path(gt=0)
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete

    db.add(todo)
    db.commit()


@app.delete(path="/delete_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    db.delete(todo)
    db.commit()
"""