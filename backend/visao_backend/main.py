"""Main module."""

import uuid

from flask import Flask
from sonora.wsgi import grpcWSGI
from visao_grpc.main_pb2 import File as grpc_File
from visao_grpc.main_pb2_grpc import VisAOServicer, add_VisAOServicer_to_server

from visao_backend.db import db
from visao_backend.models import *  # noqa: F403

db_name = 'visao.db'


app = Flask(__name__)

# For now, we just use SQLite, but in the event than we want to follow a
# client server approach, we can change to any sql provider (eg.: postgres or MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

db.init_app(app)

app.wsgi_app = grpcWSGI(app.wsgi_app, enable_cors=True)


class VisAOServicer(VisAOServicer):
    def UploadFile(self, request, context):
        return grpc_File(id=str(uuid.uuid4()))


if __name__ == "__main__":
    # Create all models, if necessary
    with app.app_context():
        db.create_all()
        db.session.commit()
    add_VisAOServicer_to_server(VisAOServicer(), app.wsgi_app)
    app.run("0.0.0.0", 8080, debug=True)
