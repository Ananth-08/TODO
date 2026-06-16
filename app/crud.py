from sqlalchemy.orm import Session
from app.models import Todo



def delete_todo(db: Session, todo_id: int):
    todo = get_todo_by_id(db, todo_id)

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo