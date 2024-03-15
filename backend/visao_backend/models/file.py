import sqlalchemy as sa

from . import BaseModel


class File(BaseModel):
    
    __tablename__ = "files"

    id = sa.Column(sa.String, primary_key=True)