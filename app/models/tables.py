from sqlalchemy import Column, String, Integer, Float, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import Base
import datetime

class Marca(Base):
	__tablename__ = 'marca'
	id = Column(Integer, primary_key=True)
	descricao = Column(String(45), nullable=False)
	create_at = Column(Date(), default=datetime.datetime.now())
	update_at = Column(Date(), onupdate=datetime.datetime.now())
	produtos = relationship("Produtos")

	def __init__(self, descricao):
		self.descricao = descricao
		self.create_at = datetime.datetime.now()
		self.update_at = datetime.datetime.now()

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s' % (self.id, self.descricao)



class Produtos(Base):
	__tablename__ = 'produtos'
	id = Column(Integer, primary_key=True)
	descricao = Column(String(45), nullable=False)
	saldo = Column(Numeric(precision=9, scale=2, decimal_return_scale=2))
	preco = Column(Numeric(precision=9, scale=3, decimal_return_scale=2))
	imagem = Column(String(20), unique=True)
	create_at = Column(Date(), default=datetime.datetime.now())
	update_at = Column(Date(), onupdate=datetime.datetime.now())
	id_marca = Column(Integer, ForeignKey('marca.id'))

	def __init__(self, descricao, marca, saldo=0, preco=0, imagem='no_image.png'):
		self.descricao = descricao
		self.id_marca = marca
		self.saldo = saldo
		self.preco = preco
		self.imagem = imagem
		self.create_at = datetime.datetime.now()
		self.update_at = datetime.datetime.now()

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s - SALDO: %f' % (self.id, self.descricao, self.fabricante, self.saldo)
