from fastapi  import FastAPI, Depends, HTTPException, Path
import models
from models import Todos
from database import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

db_dependencies = Annotated[Session, Depends(get_db)]

@app.get('/')
async def read_all(db: db_dependencies):
    return db.query(Todos).all()


@app.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependencies, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')