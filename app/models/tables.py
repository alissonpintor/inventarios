from sqlalchemy import Column, String, Integer, Float, Numeric, Date
from app import Base
import datetime

class Marca(Base):
	__tablename__ = 'marca'
	id = Column(Integer, primary_key=True)
	descricao = Column(String(45), nullable=False)
	create_at = Column(Date(), default=datetime.datetime.now())
	create_at = Column(Date(), onupdate=datetime.datetime.now())

	def __init__(self, descricao, fabricante, saldo=0, preco=0):
		self.descricao = descricao
		self.fabricante = fabricante
		self.saldo = saldo
		self.preco = preco

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s - SALDO: %f' % (self.id, self.descricao, self.fabricante, self.saldo)


class Produtos(Base):
	__tablename__ = 'produtos'
	id = Column(Integer, primary_key=True)
	descricao = Column(String(45), nullable=False)
	fabricante = Column(String(20), nullable=False)
	saldo = Column(Numeric(precision=9, scale=2, decimal_return_scale=2))
	preco = Column(Numeric(precision=9, scale=3, decimal_return_scale=2))
	imagem = Column(String(20), unique=True)
	create_at = Column(Date(), default=datetime.datetime.now())
	create_at = Column(Date(), onupdate=datetime.datetime.now())

	def __init__(self, descricao, fabricante, saldo=0, preco=0):
		self.descricao = descricao
		self.fabricante = fabricante
		self.saldo = saldo
		self.preco = preco

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s - SALDO: %f' % (self.id, self.descricao, self.fabricante, self.saldo)
