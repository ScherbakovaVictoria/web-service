from app import config, engine, Base
from sqlalchemy import  Column, Integer, String, Float, Date
from sqlalchemy.orm import Session
from app.pydantic_models import user_pd_model
from app.controllers import user_controller
from app.db_models import db_init
from sqlalchemy.orm import relationship



class User(Base):
    #__abstract__ = True
    __tablename__='users'
    id = Column(Integer, primary_key=True, index= True)
    login = Column(String)
    password_hash = Column(String)
    firstname = Column(String)
    phone = Column(String)
    email = Column(String)
    type = Column(String)

    @staticmethod 
    def get_by_id(id: int):
        with Session(engine) as session:
            user_db = session.query(User).get(id)
            if user_db == None: raise db_init.NotFoundExeption
            return user_db

    @staticmethod
    def get_by_login(login: str):
        with Session(engine) as session:
            user = session.query(User).filter_by(login=login).one()
            if user==None: raise db_init.NotFoundExeption
            return user

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "users",
    }
   



class Client(User):
    #__tablename__='clients'
    __mapper_args__ = {
        "polymorphic_identity": "clients",
    }

    
    @staticmethod
    def create(client: user_pd_model.UserRegister):
        with Session(engine) as session:
            client_db = session.query(Client).filter_by(login=client.phone_number).first()
            if client_db!=None: raise db_init.ExistExeption
            client_db = Client(firstname = client.firstname, phone=client.phone_number, login=client.phone_number,
            email=client.email, password_hash=user_controller.generate_password_hash(client.password))
            session.add(client_db)
            session.commit()

    @staticmethod
    def update(client: user_pd_model.UpdateUserProfile):
        with Session(engine) as session:
            
            client_db = session.query(Client).get(client.id)
            
            if client_db==None: 
                
                raise db_init.NotFoundExeption
            else:
                client_db.firstname = client.firstname
                client_db.phone = client.phone_number
                client_db.email = client.email
                session.add(client_db)
                session.commit()



    
        


class Admin(User):
    #__tablename__='admins'
    place = relationship('Place', backref='admin')
  
    
    __mapper_args__ = {
        "polymorphic_identity": "admins",
    }
   
    
    @staticmethod
    def create(client: user_pd_model.UserRegister):
        with Session(engine) as session:
            admin_db = session.query(Admin).filter_by(login=client.phone_number).first()
            if admin_db!=None: raise db_init.ExistExeption
            admin_db = Admin(firstname = client.firstname, phone=client.phone_number, login=client.phone_number,
            email=client.email, password_hash=user_controller.generate_password_hash(client.password))
            session.add(admin_db)
            session.commit()