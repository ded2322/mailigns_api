from fastapi import APIRouter, HTTPException, status
from fastapi_cache.decorator import cache

from app.schemas.clients_schemas import SClients, SUpdateData, SDelete
from app.dao.clients_dao import ClientsDao


router = APIRouter(prefix="/clients", tags=["Клиенты"])


@router.get("/all_client")
async def show_client():
    data_table = await ClientsDao.show_data_table()
    return data_table


@router.post("/add_client")
async def add_client(clients: SClients):
    await ClientsDao.insert_data(username=clients.name, email=clients.email)
    return {"message": "Клиент успешно добавлен"}


@router.patch("/update_data")
async def update_data(update: SUpdateData):
    data_user = await ClientsDao.found_one(id=update.id)
    if not data_user:
        raise HTTPException(status_code=404)
    await ClientsDao.update_email(update.id, update.new_email)

    return {"message": "почта успешно изменена"}


@router.delete("/delete_clients")
async def delete_clients(data_client: SDelete):
    data_user = await ClientsDao.found_one(id=data_client.id)
    if not data_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого пользователя не существует",
        )
    await ClientsDao.delete_date(id=data_client.id)

    return {"message": "клинет успешно удален"}
