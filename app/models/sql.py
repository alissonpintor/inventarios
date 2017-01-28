from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.types import CHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()
engine = create_engine("db2+ibm_db://dba:overhead@192.168.104.3:50000/STOKY")

class Marca(Base):
	__tablename__ = 'marca'
	id = Column('IDMARCAFABRICANTE', Integer, primary_key=True)
	descricao = Column('DESCRICAO', String(40), nullable=False)
	flagInativo = Column('FLAGINATIVO', CHAR(1), nullable=False)
	flagExporta = Column('FLAGEXPORTADADOSSUVINIL', CHAR(1), nullable=False)
	dtalteracao = Column('DTALTERACAO', Date())

	seq_id = None

	def __init__(self, descricao, flagInativo='F', flagExporta='F', dtalteracao=datetime.datetime.now()):
		self.id = self.next_id()
		self.descricao = descricao
		self.flagInativo = flagInativo
		self.flagExporta = flagExporta
		self.dtalteracao = dtalteracao

	def next_id(self):
		if(Marca.seq_id == None):
			from sqlalchemy.sql.expression import func
			Base.metadata.create_all(engine)
			Session = sessionmaker(bind=engine)
			se = Session()
			Marca.seq_id = se.query(func.max(Marca.id)).one()[0]
		Marca.seq_id += 1
		return Marca.seq_id

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s' % (self.id, self.descricao)


class ProdutosCiss(Base):
	__tablename__ = 'produtos_view'
	id = Column('idsubproduto', Integer, primary_key=True)
	descricao = Column('descricaoproduto', String(45), nullable=False)
	fabricante = Column('FABRICANTE', String(20), nullable=False)

	def __init__(self, descricao, fabricante):
		self.descricao = descricao
		self.fabricante = fabricante

	def __repr__(self):
		return 'ID: %d - DESCRICAO: %s - MARCA: %s' % (self.idsubproduto, self.descricaoproduto, self.fabricante)

'''
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

se = Session()

produto = se.query(ProdutosCiss).filter(ProdutosCiss.idsubproduto == 13504).all()

for p in produto:
	print(p.idsubproduto)
	print(p.descricaoproduto)
	print(p.fabricante)

m = Marca('Teste Alisson')
print(m.id)
print(m.descricao)
print(m.flagInativo)
print(m.dtalteracao)

se.add(m)
se.commit()
'''
