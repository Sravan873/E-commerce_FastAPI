from sqlalchemy import Column, Integer, String, Float,Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    brand = Column(String(100), nullable=False)

class User(Base):
    __tablename__ = "users"

    user_name = Column(String(100), primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(100), nullable = False, default = "user")  # Default role is "user"
    is_active = Column(Boolean, default=False, nullable = False)