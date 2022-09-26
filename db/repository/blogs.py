from sqlalchemy.orm import Session

from schemas.blogs import BlogCreate
from db.models.blogs import Blog


def create_new_blog(blog: BlogCreate, db: Session, owner_id: int):
    blog_object = Blog(**dict(), owner_id=owner_id)
    db.add(blog_object)
    db.commit()
    db.refresh(blog_object)
    return blog_object
