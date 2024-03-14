#!/bin/bash

poetry run python -m grpc_tools.protoc -I../grpc ../grpc/main.proto --python_out=visao_backend/visao_grpc --grpc_python_out=visao_backend/visao_grpc

poetry run protol \
  --create-package \
  --in-place \
  --python-out visao_backend/visao_grpc \
  protoc --proto-path=../grpc ../grpc/main.proto