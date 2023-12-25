from sqlalchemy.orm import Session
from src.modules.sneakers.schema import SneakerSchema
from src.db.models.sneaker import Sneaker as SneakerModel
from src.db.repositories.sneaker_repository import SneakerRepository
from src.modules.base_service import BaseService

class SneakerService(BaseService):
    def __init__(self, db: Session):
        super().__init__()
        self.sneaker_repository = SneakerRepository(db)

    def get_sneakers(self):
        sneakers = self.sneaker_repository.find_all()
        return (
            self.response_builder.status(True)
            .code(200)
            .message('Sneakers retrieved successfully')
            .data(sneakers)
            .build()
        )
    
    def add_sneaker(self, payload: SneakerSchema):
        sneaker = self.sneaker_repository.create(payload.dict())
        return (
            self.response_builder.status(True)
            .code(201)
            .message('Sneakers added successfully')
            .data(sneaker)
            .build()
        )
