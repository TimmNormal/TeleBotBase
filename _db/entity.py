from email.policy import default
from sqlalchemy import  Column, DateTime, Integer, String, ForeignKey, Float,Boolean,create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import Session





Base = declarative_base()

class Buy(Base):
    __tablename__ = 'buy'
    
    id = Column(Integer, primary_key=True,nullable=False,autoincrement=True)
    
    user_id = Column(String,nullable = False)
    user_name = Column(String,nullable=False)
    date = Column(DateTime,nullable=False,default = func.now())
    price = Column(Integer,nullable=False)
    
    image = Column(String,nullable=True)
    comment = Column(String,nullable=True)

    is_minus = Column(Boolean,nullable=False,server_default = sqlalchemy.text("true"))

class BuyItem(Base):
    __tablename__ = "buy_item"

    id = Column(Integer, primary_key=True,nullable=False,autoincrement=True)

    name = Column(String, nullable=False)
    type_item = Column(Integer,ForeignKey("item_type.id"), nullable=True)
    

class ItemType(Base):
    __tablename__ = "item_type"

    id = Column(Integer, primary_key=True,nullable=False,autoincrement=True)

    name = Column(String, nullable=False)

class UserAction(Base):
    __tablename__ = "user_action"

    id = Column(Integer, primary_key=True,nullable=False,autoincrement=True)

    name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)

if __name__ == '__main__':
    from conf import DB_NAME, HOST, PASSWORD, USER

    engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
    Base.metadata.create_all(engine)

    engine.connect()
    session = Session(bind=engine)

