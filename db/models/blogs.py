from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.base_class import Base


class Blog(Base):
    _id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    date_posted = Column(Date)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="blogs")
