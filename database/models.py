from sqlalchemy import String, Text, Float, DateTime, func, ForeignKey, BigInteger, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """
    Создание и обновление таблицы продуктов
    """
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Banner(Base):
    """
    Настройки таблицы баннера
    """
    __tablename__ = 'banner'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Category(Base):
    """
    Настройки таблицы категорий
    """
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)


class Product(Base):
    """
    Настройки таблицы продуктов
    """
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # Уникальный идентификатор продукта,
    # не пустой
    name: Mapped[str] = mapped_column(String(150), nullable=False)  # Наименование продукта, не пустое
    description: Mapped[str] = mapped_column(Text)  # Описание продукта
    price: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)  # Стоимость продукта, не пустое
    image: Mapped[str] = mapped_column(String(150))  # Путь к изображению продукта
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    category: Mapped['Category'] = relationship(backref='product')


class User(Base):
    """
    Настройки таблицы пользователей
    """
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone: Mapped[str] = mapped_column(String(13), nullable=True)


class Cart(Base):
    """
    Настройки таблицы корзины
    """
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    quantity: Mapped[int]
    user: Mapped['User'] = relationship(backref='cart')
    product: Mapped['Product'] = relationship(backref='cart')
