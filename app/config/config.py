#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
#
#
import os, configparser
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

async def initiate_database():
    USR = os.getenv('MONGO_USR')
    PASS = os.getenv('MONGO_PASS')
    HOST = os.getenv('MONGO_HOST')
    PORT = os.getenv('MONGO_PORT')
    DB =  os.getenv('MONGO_DB')

    mongo_uri = f'mongodb://{USR}:{PASS}@{HOST}:{PORT}/{DB}'
    client = AsyncIOMotorClient(mongo_uri)

