from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.models import Base
from app.schemas import (
    TodoCreate,
    TodoResponse
)
from app import crud


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Todo API Running Successfully"
    }


# GET ALL TODOS
@app.get(
    "/todos",
    response_model=list[TodoResponse]
)
def get_todos(
    completed: bool | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_todos(
        db,
        completed
    )


# GET TODO BY ID
@app.get(
    "/todos/{todo_id}",
    response_model=TodoResponse
)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = crud.get_todo_by_id(
        db,
        todo_id
    )

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


# CREATE TODO
@app.post(
    "/todos",
    response_model=TodoResponse
)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return crud.create_todo(
        db,
        todo.title,
        todo.completed
    )