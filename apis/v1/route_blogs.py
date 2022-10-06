from fastapi import APIRouter
from db.repository.blogs import create_new_blog
from schemas.blogs import BlogCreate_schema, ShowBlog

router = APIRouter()


@router.post("/create-blog/", response_model=ShowBlog)
def create_blog(blog: BlogCreate_schema):
    current_user = 1
    blog = create_new_blog(blog=blog, owner_id=current_user)
    return blog
