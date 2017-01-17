from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)
#from app import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True, nullable=False)
	hashed = Column(String(50), nullable=False)
	salt = Column(String(50), nullable=False)

	def __init__(self, username, hashed, salt):
		self.username = username
		self.hashed = hashed
		self.salt = salt

	def __repr__(self):
		return '<User: %s> <Passwd: %s>' % (self.username, self.hashed)

class Produtos(Base):
	__tablename__ = 'produtos'
	id = Column(Integer, primary_key=True)
	descricao = Column(String(45), nullable=False)
	fabricante = Column(String(20), nullable=False)
	saldo = Column(Float())

	def __init__(self, descricao, fabricante, saldo):
		self.descricao = descricao
		self.fabricante = fabricante
		self.saldo = saldo

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
