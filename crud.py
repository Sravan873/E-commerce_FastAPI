from sqlalchemy.orm import Session
from models import Product, User
import schemas
import bcrypt
from fastapi import HTTPException, Response
import jwt
SECRET_KEY="abcdefghijklmnopqrtuvwxyz"
ALGORITHM="HS256"


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()


def get_by_category(db: Session, category: str):
    return db.query(Product).filter(
        Product.category == category
    ).all()


def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    db_product.name = product.name
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock = product.stock
    db_product.brand = product.brand

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product



def user_register(db: Session, user: schemas.UserCreate): #validate the iputs that are come from the user and then store the data in the database

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(   #hashpw is used to hash the password with the salt and then decode it
      user.password.encode("utf-8"),
        salt
    ).decode("utf-8")

    db_user = User(   # in this instatntiation of the User class sqlalchemy recognizes that is base class metadata and create python object and ORM create python objects for columns 
        user_name=user.user_name,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)   #it is used to add the new user instance object to the database
    db.commit()
    db.refresh(db_user)

    return db_user

def user_login(db: Session , user: schemas.Userlogin, response: Response):
    user_exist = db.query(User).filter(User.email == user.email).first()
    is_same =  bcrypt.checkpw(user.password.encode(),user_exist.hashed_password.encode())
    if is_same:
        payload = {
            "user_name": user_exist.user_name,
            "email": user_exist.email,
            "role": user_exist.role
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        response.set_cookie(key="access_token",value=token)
        return "login successful!"
    return "Invalid password"