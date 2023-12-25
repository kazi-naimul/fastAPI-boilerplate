from loguru import logger
from fastapi import Depends, APIRouter, HTTPException
from src.configs.auth import verify_token
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.db.models.sneaker import Sneaker as SneakerModel
from src.modules.sneakers.schema import SneakerSchema
from src.modules.sneakers.sneaker_service import SneakerService


router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/sneakers", status_code=200)
async def get_sneakers(db: Session = Depends(get_db)):

    """
    gets all the sneakers listed in the database.

    Returns:
        list: An array of sneakers' objects.
    """
    sneaker_service = SneakerService(db)

    return sneaker_service.get_sneakers()


@router.post("/sneakers", status_code=201)
async def add_sneaker(payload: SneakerSchema, db: Session = Depends(get_db)):

    """
    Add sneaker in the database.

    Returns:
        Object: same payload which was sent with 201 status code on success.
    """

    sneaker_service = SneakerService(db)
    return sneaker_service.add_sneaker(payload)


@router.put("/sneakers/{sneaker_id}", status_code=201)
async def update_sneaker(
    sneaker_id: int, payload: SneakerSchema, db: Session = Depends(get_db)
):

    """
    Updates the sneaker object in db

    Raises:
        HTTPException: 404 if sneaker id is not found in the db

    Returns:
        object: updated sneaker object with 201 status code
    """

    sneaker = db.query(SneakerModel).filter(SneakerModel.id == sneaker_id).first()
    if not sneaker:
        desc = "Sneaker not found"
        logger.error(desc)
        raise HTTPException(status_code=404, detail=desc)

    sneaker.brand_name = payload.brand_name
    sneaker.name = payload.name
    sneaker.description = payload.description
    sneaker.size = payload.size
    sneaker.color = payload.color
    sneaker.free_delivery = payload.free_delivery
    db.commit()

    logger.success("Updated a sneaker.")
    return sneaker


@router.delete("/sneakers/{sneaker_id}", status_code=204)
async def delete_sneaker(sneaker_id: int, db: Session = Depends(get_db)):
    """
    Deletes the sneaker object from db

    Raises:
        HTTPException: 404 if sneaker id is not found in the db

    Returns:
        Object: Deleted true with 204 status code
    """

    sneaker = db.query(SneakerModel).filter(SneakerModel.id == sneaker_id).first()
    if not sneaker:
        desc = "Sneaker not found"
        logger.error(desc)
        raise HTTPException(status_code=404, detail=desc)
    db.delete(sneaker)
    db.commit()

    logger.success("Deleted a sneaker.")

    return {"Deleted": True}
