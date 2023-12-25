from sqlalchemy.orm import Session
from src.db.session import get_db
from sqlalchemy import update
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from typing import Optional, List

Base: DeclarativeMeta = declarative_base()

class BaseRepository:
    def __init__(self, model, db: Session):
        self.model = model
        self.db = db

    def query(self):
        return self.db.query(self.model)

    def find_all(self):
        return self.query().all()

    def find_by_id(self, item_id: int) -> Optional:
        return self.query().filter(self.model.id == item_id).first()

    def find_one_by_where(
        self, where: dict, order_by: dict = None
    ) -> Optional:
        query = self.query().filter_by(**where)
        if order_by:
            query = query.order_by(
                *[getattr(self.model, field).asc() if order == 'ASC' else getattr(self.model, field).desc()
                  for field, order in order_by.items()]
            )
        return query.first()

    def find_by_where(
        self, where: dict, order_by: dict = None
    ) -> List:
        query = self.query().filter_by(**where)
        if order_by:
            query = query.order_by(
                *[getattr(self.model, field).asc() if order == 'ASC' else getattr(self.model, field).desc()
                  for field, order in order_by.items()]
            )
        return query.all()

    def update_where(self, where: dict, update_data: dict):
        try:
            stmt = update(self.model).where(**where).values(update_data)
            self.db.execute(stmt)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def update_by_id(self, item_id: int, update_data: dict):
        try:
            stmt = update(self.model).where(self.model.id == item_id).values(update_data)
            self.db.execute(stmt)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def create(self, data: dict):
        try:
            instance = self.model(**data)
            self.db.add(instance)
            self.db.commit()
            self.db.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def delete_by_where(self, where: dict):
        try:
            stmt = self.model.__table__.delete().where(**where)
            self.db.execute(stmt)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def bulk_create(self, data_list: List[dict]):
        try:
            stmt = insert(self.model).values(data_list)
            self.db.execute(stmt)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def truncate(self):
        try:
            stmt = self.model.__table__.delete()
            self.db.execute(stmt)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def run_raw_query(self, query: str, arg=None):
        try:
            result = self.db.execute(query, arg)
            return result.fetchall() if result else None
        except SQLAlchemyError as e:
            db.rollback()
            raise e

