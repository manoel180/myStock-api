import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from infra.config import setting


database_username = setting.db_usr
database_password = setting.db_pwd
database_ip       = setting.db_host
database_name     = setting.db_name
database_port     = setting.db_port

engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.
    format(database_username, database_password, database_ip, database_port, database_name))

SessionLocal = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()