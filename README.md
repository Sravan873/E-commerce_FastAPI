🛒 FastAPI Product Management API with MySQL

A beginner-friendly REST API project built using **FastAPI, MySQL, SQLAlchemy, and Pydantic**. This project demonstrates how to connect FastAPI with a MySQL database and perform complete CRUD (Create, Read, Update, Delete) operations on an E-Commerce Product Management System.

---

📌 Project Overview

This project was developed as part of my backend development learning journey. It demonstrates how to build REST APIs, connect them to a MySQL database, validate incoming data using Pydantic, and perform database operations using SQLAlchemy ORM.

The project manages product information in an E-Commerce application and includes complete CRUD functionality along with category-based product filtering.

---

🛠️ Tech Stack

- Python 3.x
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- PyMySQL
- Uvicorn
- Swagger UI
- Requests Library

---

📁 Project Structure

```text
E_commerce/
│
├── main.py              # Main FastAPI application
├── database.py          # Database connection configuration
├── models.py            # SQLAlchemy database model
├── schemas.py           # Pydantic schemas
├── crud.py              # CRUD operations
├── requirements.txt
├── .gitignore
└── README.md
```

---

⚙️ Features

- ✅ FastAPI project setup
- ✅ MySQL database connection
- ✅ SQLAlchemy ORM integration
- ✅ Pydantic request validation
- ✅ Create Product API
- ✅ View All Products API
- ✅ View Product by ID API
- ✅ Update Product API
- ✅ Delete Product API
- ✅ Search Products by Category
- ✅ Automatic Swagger Documentation
- ✅ Clean Project Structure
- ✅ Dependency Injection using `Depends()`

---

🗄️ Database Table

Products

| Column | Type |
|---------|------|
| id | Integer (Primary Key) |
| name | String |
| category | String |
| price | Float |
| stock | Integer |
| brand | String |

---

📚 Files Explanation

database.py

Responsible for:

- Creating MySQL database connection
- Creating SQLAlchemy Engine
- Creating database sessions
- Providing database dependency to FastAPI

Example:

```python
DATABASE_URL = "mysql+pymysql://root:Sravan%400421@localhost:3306/E_commerce"
```

---

models.py

Defines the Product table using SQLAlchemy ORM.

```python
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)
    brand = Column(String(100))
```

---

schemas.py

Defines request validation and response models using Pydantic.

```python
class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    brand: str
```

```python
class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
```

---

crud.py

Contains all database operations.

Implemented CRUD Functions:

- Create Product
- Get All Products
- Get Product by ID
- Update Product
- Delete Product
- Get Products by Category

---

main.py

Contains all FastAPI routes and API endpoints.

Responsible for:

- Creating FastAPI application
- Database dependency injection
- Routing requests
- Exception handling
- Returning API responses

---

🚀 API Endpoints

Home

GET /

Response

```json
"Welcome to Product Management API"
```

---

Create Product

POST /products

Sample Request

```json
{
    "name": "iPhone 16",
    "category": "Mobiles",
    "price": 79999,
    "stock": 25,
    "brand": "Apple"
}
```

Sample Response

```json
{
    "id": 1,
    "name": "iPhone 16",
    "category": "Mobiles",
    "price": 79999,
    "stock": 25,
    "brand": "Apple"
}
```

---

Get All Products

GET /products

Sample Response

```json
[
    {
        "id": 1,
        "name": "iPhone 16",
        "category": "Mobiles",
        "price": 79999,
        "stock": 25,
        "brand": "Apple"
    }
]
```

---

Get Product by ID

GET /products/{product_id}

Example

```
GET /products/1
```

---

Update Product

PUT /products/{product_id}

Sample Request

```json
{
    "name": "Samsung Galaxy S25 Ultra",
    "category": "Mobiles",
    "price": 109999,
    "stock": 15,
    "brand": "Samsung"
}
```

---

Delete Product

DELETE /products/{product_id}

Example

```
DELETE /products/1
```

Response

```json
{
    "message": "Product deleted successfully"
}
```

---

Get Products by Category

GET /category/{category}

Example

```
GET /category/Mobiles
```

Sample Response

```json
[
    {
        "id": 1,
        "name": "iPhone 16",
        "category": "Mobiles",
        "price": 79999,
        "stock": 25,
        "brand": "Apple"
    }
]
```

---

🧪 Testing APIs Using Python Requests

Get All Products

```python
import requests

response = requests.get("http://127.0.0.1:8000/products")
print(response.json())
```

Get Product by ID

```python
import requests

response = requests.get("http://127.0.0.1:8000/products/1")
print(response.json())
```

Create Product

```python
import requests

data = {
    "name":"Dell Laptop",
    "category":"Laptops",
    "price":65000,
    "stock":10,
    "brand":"Dell"
}

response = requests.post(
    "http://127.0.0.1:8000/products",
    json=data
)

print(response.json())
```

Update Product

```python
import requests

data = {
    "name":"Gaming Laptop",
    "category":"Laptops",
    "price":85000,
    "stock":8,
    "brand":"ASUS"
}

response = requests.put(
    "http://127.0.0.1:8000/products/1",
    json=data
)

print(response.json())
```

Delete Product

```python
import requests

response = requests.delete(
    "http://127.0.0.1:8000/products/1"
)

print(response.json())
```

Get Products by Category

```python
import requests

response = requests.get(
    "http://127.0.0.1:8000/category/Mobiles"
)

print(response.json())
```

---

▶️ How to Run the Project

1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-fastapi.git
```

2. Navigate to the Project

```bash
cd E_commerce
```

3. Create a Virtual Environment

```bash
python -m venv fastapi_env
```

Activate it

Windows

```bash
fastapi_env\Scripts\activate
```

4. Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql
pip install requests
```

or

```bash
pip install -r requirements.txt
```

5. Configure MySQL

Create the database.

```sql
CREATE DATABASE E_commerce;
```

Update the database credentials in `database.py`.

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/E_commerce"
```

6. Run the Server

```bash
uvicorn main:app --reload
```

7. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

📸 Output

Swagger UI allows you to:

- Create Product
- View All Products
- View Product by ID
- Update Product
- Delete Product
- Search Products by Category
- Test APIs without Postman

---

🎯 Learning Outcomes

Through this project, I learned:

- FastAPI Fundamentals
- REST API Development
- SQLAlchemy ORM
- MySQL Database Connectivity
- Dependency Injection
- CRUD Operations
- Pydantic Schema Validation
- API Documentation with Swagger UI
- Database Session Management
- Project Organization

---

🚧 Future Improvements

- Product Image Upload
- Authentication using JWT
- User Management
- Shopping Cart Module
- Orders Module
- Categories Table
- Pagination
- Search by Brand
- Price Range Filter
- Product Sorting
- Docker Deployment



👨‍💻 Author

**Potharaju Sravan Varma**

B.Tech (EEE) | Python Developer | FastAPI Learner | Aspiring Software Developer

GitHub: https://github.com/Sravan873

LinkedIn: https://www.linkedin.com/in/sravanvarma-potharju


⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to build and share more projects!

---

📄 License

This project is created for learning and educational purposes.