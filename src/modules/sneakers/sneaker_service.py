from loguru import logger
from sqlalchemy.orm import Session
from src.modules.sneakers.schema import SneakerSchema
from src.db.models.sneaker import Sneaker as SneakerModel
from src.db.repositories.sneaker_repository import SneakerRepository
from src.modules.base_service import BaseService
from fastapi import HTTPException

class SneakerService(BaseService):
    def __init__(self, db: Session):
        super().__init__()
        self.sneaker_repository = SneakerRepository(db)

    def get_sneakers(self):
        try:
            sneakers = self.sneaker_repository.find_all()
            return (
                self.response_builder.status(True)
                .code(200)
                .message('Sneakers retrieved successfully')
                .data(sneakers)
                .build()
            )
        except HTTPException as http_exception:
            raise http_exception  # Re-raise the HTTPException to let FastAPI handle the response
        except Exception as e:
            logger.error(e)
            return (
                self.response_builder.status(False)
                .code(500)
                .message('Internal server error')
                .build()
            )
    
    def add_sneaker(self, payload: SneakerSchema):
        try:
            sneaker = self.sneaker_repository.find_one_by_where({'name': payload.name})
            if sneaker:
                return (
                    self.response_builder.status(False)
                    .code(400)
                    .message('Sneaker already exists')
                    .build()
                )
            sneaker = self.sneaker_repository.create(payload.dict())
            return (
                self.response_builder.status(True)
                .code(201)
                .message('Sneakers added successfully')
                .data(sneaker)
                .build()
            )
        except HTTPException as http_exception:
            raise http_exception  # Re-raise the HTTPException to let FastAPI handle the response
        except Exception as e:
            print(e)
            logger.error(e)
            return (
                self.response_builder.status(False)
                .code(500)
                .message('Internal server error')
                .build()
            )
    
    def update_sneaker(self, sneaker_id: int, payload: SneakerSchema):
        try:
            sneaker = self.sneaker_repository.find_one_by_where({'id': sneaker_id})
            if not sneaker:
                return (self.response_builder.status(False)
                    .code(404)
                    .message('Sneaker not found')
                    .build()
                )
            if sneaker.name != payload.name:
                sneaker = self.sneaker_repository.find_one_by_where({'name': payload.name})
                if sneaker:
                    return (
                        self.response_builder.status(False)
                        .code(400)
                        .message('Sneaker already exists')
                        .build()
                    )
            sneaker = self.sneaker_repository.update_by_id(sneaker_id, payload.dict())
            return (
                self.response_builder.status(True)
                .code(200)
                .message('Sneakers updated successfully')
                .build()
            )
        except HTTPException as http_exception:
            raise http_exception  # Re-raise the HTTPException to let FastAPI handle the response
        except Exception as e:
            logger.error(e)
            return (
                self.response_builder.status(False)
                .code(500)
                .message('Internal server error')
                .build()
            )
       
    
    def delete_sneaker(self, sneaker_id: int):
        try:
            sneaker = self.sneaker_repository.find_one_by_where({'id': sneaker_id})
            if not sneaker:
                return (self.response_builder.status(False)
                    .code(404)
                    .message('Sneaker not found')
                    .build()
                )
            sneaker = self.sneaker_repository.delete_by_where({'id': sneaker_id})
            return (
                self.response_builder.status(True)
                .code(200)
                .message('Sneakers deleted successfully')
                .build()
            )
        except HTTPException as http_exception:
            raise http_exception  # Re-raise the HTTPException to let FastAPI handle the response
        except Exception as e:
            logger.error(e)
            return (
                self.response_builder.status(False)
                .code(500)
                .message('Internal server error')
                .build()
            )
