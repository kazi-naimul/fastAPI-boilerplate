import os
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

from src.libraries.logger.logger_builder import init_logging
from src.router import load_routers

load_dotenv(".env")

root_router = APIRouter()

app = FastAPI(title="FastAPI Boiler Plate")
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# Load routers using the external function
load_routers(app)

app.include_router(root_router)

init_logging()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
