#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
# By Checchia - 09/2023
#
import os, configparser
from datetime import datetime
from fastapi import FastAPI, Body, Response, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from config.config import initiate_database
from utils.errordict import create_database_if_not_exists, http_error

app = FastAPI(
    title = os.getenv('TITLE'),
    description= os.getenv('DESCRIPTION'),
    version= os.getenv('VERSION'),
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def start_database():
    create_database_if_not_exists()
    await initiate_database()
    print("Conexão com o banco de dados estabelecida.")

# Evento de encerramento
@app.on_event("shutdown")
async def shutdown_database():
    # Lógica para fechar a conexão com o banco de dados, se necessário
    print("Conexão com o banco de dados encerrada.")

@app.middleware("http")
async def measure_time(request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    end_time = datetime.now()
    execution_time = end_time - start_time
    response.headers["X-Execution-Time"] = str(execution_time)
    return response


@app.get("/", tags=["/"])
async def api_root():
    import time
    dataBase = "0.0005 ms"
    postFix = "0.0001 ms"
    DATA = {"message": "OK"}
    return {
        "status_code": status.HTTP_200_OK,
        "description": "Done!",
        "data": DATA,
    }

@app.get("/healthcheck", tags=["/"])
async def valida_healthcheck():
    dataBase = "0.0005 ms"
    postFix = "0.0001 ms"
    DATA = {"database": dataBase, "smtp": postFix}
    return {
        "status_code": status.HTTP_200_OK,
        "description": "Healthcheck done!",
        "data": DATA,
    }

@app.get("/error/{code}", tags=["/"])
async def get_error_code(code):
    result = http_error(code)

    DATA = {"message": "OK", "result": result}
    return {
        "status_code": status.HTTP_200_OK,
        "description": "Done!",
        "data": DATA,
    }

#app.include_router(loginRouter, tags=["login"], prefix="/login")
#app.include_router(emailRouter, tags=["e-mail"], prefix="/email", dependencies=[Depends(token_listener)],)
