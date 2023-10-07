#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
#
#
import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from utils.vault import get_vault

async def initiate_database():
    MONGODB = get_vault("MONGODB")
    user = MONGODB['MONGO_USR']
    password = MONGODB['MONGO_PASS']
    host = MONGODB['MONGO_HOST']
    port = MONGODB['MONGO_PORT']
    db = MONGODB['MONGO_DB']

    mongo_uri = f'mongodb://{user}:{password}@{host}:{port}/{db}'
    client = AsyncIOMotorClient(mongo_uri)

