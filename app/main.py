from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.models import Base
from app.schemas import (
    TodoCreate,
    TodoUpdate,
    TodoResponse
)
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = crud.delete_todo(db, todo_id)

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": f"Todo {todo_id} deleted successfully"
    }