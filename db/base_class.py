from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# Every model will inherit this 'Base' class and we will utilize this base
# class to create all the database tables. Also, we will keep all common logic
# related to tables in this 'Base' class. For instance, all our table tables will
# have an id field. This will be used to uniquely identify each row/record.
