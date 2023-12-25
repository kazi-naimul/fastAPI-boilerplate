from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from src.db.session import Base
from sqlalchemy.orm import declarative_base
from src.db.models.sneaker import Sneaker as SneakerModel
from src.db.repositories.base_repository import BaseRepository

Base = declarative_base()

class SneakerRepository(BaseRepository):
    def __init__(self, db:Session):
        super().__init__(SneakerModel, db)
