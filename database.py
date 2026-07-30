from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# DATABASE_URL="mysql+pymysql://root:Sravan%400421@localhost:3306/E_commerce"

DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_js0zIjQX4GvWk5mMhL3@mysql-22b8dc21-sravanvarma042117-7ec0.e.aivencloud.com:11523/defaultdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
