"""Main module."""
from visao_grpc.main_pb2_grpc import VisAOServicer, add_VisAOServicer_to_server
from visao_grpc.main_pb2 import File
from sonora.wsgi import grpcWSGI
import grpc
from concurrent import futures
from flask import Flask, Blueprint
import uuid


app = Flask(__name__)

app.wsgi_app = grpcWSGI(app.wsgi_app, enable_cors=True)

class VisAOServicer(VisAOServicer):
    def GetImages(self, request, context):
        return super().GetImages(request, context)

    def UploadFile(self, request, context):
        return File(id=str(uuid.uuid4()))

if __name__ == "__main__":
    add_VisAOServicer_to_server(VisAOServicer(), app.wsgi_app)
    app.run("0.0.0.0", 8080, debug=True)
