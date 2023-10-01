#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
# By Checchia - 09/2023
#
import os, configparser
from fastapi import FastAPI, Body, Response, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.config import initiate_database

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
    await initiate_database()
    print("Conexão com o banco de dados estabelecida.")

# Evento de encerramento
@app.on_event("shutdown")
async def shutdown_database():
    # Lógica para fechar a conexão com o banco de dados, se necessário
    print("Conexão com o banco de dados encerrada.")


@app.get("/", tags=["/"])
async def api_root():
    dataBase = "0.0005 ms"
    postFix = "0.0001 ms"
    DATA = {"message": "OK"}
    return {
        "data": DATA,
        "status_code": status.HTTP_200_OK,
        "response_type": "success",
        "description": "Done!",

    }

@app.get("/healthcheck", tags=["/"])
async def valida_healthcheck():
    dataBase = "0.0005 ms"
    postFix = "0.0001 ms"
    DATA = {"database": dataBase, "smtp": postFix}
    return {
        "status_code": status.HTTP_200_OK,
        "response_type": "success",
        "description": "Healthcheck done!",
        "data": DATA,
    }

#app.include_router(loginRouter, tags=["login"], prefix="/login")
#app.include_router(emailRouter, tags=["e-mail"], prefix="/email", dependencies=[Depends(token_listener)],)
