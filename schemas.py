from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    brand: str


class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class UserCreate(BaseModel):
    user_name : str
    email: str
    password: str
    # is_admin : bool
    # is_active : bool

class Userlogin(BaseModel):
    email: str
    password: str

class UserResponse(UserCreate):
    user_name: str
    email: str
    role: str
    is_active: bool
    model_config = {
        "from_attributes": True
    }