from flask_sqlalchemy import SQLAlchemy

from visao_backend.models import BaseModel

db = SQLAlchemy(model_class=BaseModel)
