from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Product


async def orm_add_product(session: AsyncSession, data: dict):
    """
    Добавляем произвольный товар в базу данных
    """
    obj = Product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        image=data['image']
    )
    session.add(obj)
    await session.commit()


async def orm_get_products(session: AsyncSession):
    """
    Получаем все товары из базы данных
    """
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_product(session: AsyncSession, product_id: int):
    """
    Получаем товар из базы данных по id
    """
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar_one()


async def orm_update_product(session: AsyncSession, product_id: int, data):
    """
    Обновляем товар в базе данных по id
    """
    query = update(Product).where(Product.id == product_id).values(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        image=data['image'])
    await session.execute(query)
    await session.commit()


async def orm_delete_product(session: AsyncSession, product_id: int):
    """
    Удаляем товар из базы данных по id
    """
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()
