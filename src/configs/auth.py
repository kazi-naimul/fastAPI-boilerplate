import os
from dotenv import load_dotenv
from fastapi import Header, HTTPException
from src.libraries.response.response_builder import ResponseBuilder

load_dotenv(".env")

X_TOKEN = os.environ["X_TOKEN"]


async def verify_token(x_token: str = Header()):
    if x_token != X_TOKEN:
        return (
                ResponseBuilder().status(False)
                .code(400)
                .message('X-Token header invalid')
                .build()
            )
