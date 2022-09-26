from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from db.db_config import get_db
from db.repository.blogs import create_new_blog
from schemas.blogs import BlogCreate, ShowBlog

router = APIRouter()


@router.post("/create-blog/", response_model=ShowBlog)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    current_user = 1
    blog = create_new_blog(blog=blog, db=db, owner_id=current_user)
    return blog
