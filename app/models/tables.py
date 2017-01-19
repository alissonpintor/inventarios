from sqlalchemy import Column, String, Integer, Float
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Base = declarative_base()
#engine = create_engine('sqlite:///database.db', echo=True)
#engine = create_engine("db2+ibm_db://relatorio:relatorio@192.168.104.3:50000/STOKY")
from app import Base

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

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s - SALDO: %f' % (self.id, self.descricao, self.fabricante, self.saldo)


'''
class ProdutosCiss(Base):
	__tablename__ = 'dba.produtos_view'
	idsubproduto = Column(Integer, primary_key=True)
	descricaoproduto = Column(String(45), nullable=False)
	fabricante = Column(String(20), nullable=False)

	def __init__(self, descricao, fabricante, saldo):
		self.descricao = descricao
		self.fabricante = fabricante
		self.saldo = saldo

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s' % (self.id, self.descricao, self.fabricante)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
'''
