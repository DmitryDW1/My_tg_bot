from sqlalchemy import String, Text, Float, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

"""
Создание и обновление таблицы продуктов 
"""


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


""" 
Настройки таблицы продуктов 
"""


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # Уникальный идентификатор продукта,
    # не пустой
    name: Mapped[str] = mapped_column(String(150), nullable=False)  # Наименование продукта, не пустое
    description: Mapped[str] = mapped_column(Text)  # Описание продукта
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)  # Стоимость продукта, не пустое
    image: Mapped[str] = mapped_column(String(150))  # Путь к изображению продукта
