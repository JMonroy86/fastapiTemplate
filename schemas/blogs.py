from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class BlogBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Blog
class BlogCreate_schema(BlogBase):
    title: str
    body: str


# this will be used to format the response to not to have id,owner_id etc
class ShowBlog(BlogBase):
    title: str
    body: str
    date_posted: date

    class Config:  # to convert non dict obj to json
        orm_mode = True
