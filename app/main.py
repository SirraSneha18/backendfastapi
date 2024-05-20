from fastapi import FastAPI
import logging
import os

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logging.info(f"Current working directory: {os.getcwd()}")
logging.info(f"Directory contents: {os.listdir(os.getcwd())}")

@app.get("/")
def read_root():
    return {"Hello": "World"}
