
from abc import abstractmethod

from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class BaseModel(DeclarativeBase, MappedAsDataclass):

    @abstractmethod
    def to_gRPC(self):
        raise NotImplementedError("This model has not implemented to_gRPC method")
    
    @staticmethod
    @abstractmethod
    def from_gRPC(grpc_object):
        raise NotImplementedError("This model has not implemented from_gRPC method")
