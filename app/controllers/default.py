import bcrypt
from app import app
from app.models.tables import Produtos, Marca
from sqlalchemy.ext.declarative import DeclarativeMeta
from bottle import template, static_file, request, redirect
import json
from datetime import datetime

# INICIO converter classe SQLAlchemy em json ##################################
class AlchemyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj.__class__, DeclarativeMeta):
			# an SQLAlchemy class
			fields = {}
			for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
				data = obj.__getattribute__(field)
				if isinstance(data.__class__, datetime):
					data = data.__str__
					print(data)
				try:
					json.dumps(data) # this will fail on non-encodable values, like other classes
					fields[field] = data
				except TypeError:
					fields[field] = None
			# a json-encodable dict
			return fields
		return json.JSONEncoder.default(self, obj)
# FINAL converter classe SQLAlchemy em json ###################################

# INICIO static routes ########################################################
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='app/static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='app/static/js')

@app.get('/<filename:re:.*\.json>')
def javascripts(filename):
	return static_file(filename, root='app/static/json')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='app/static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
	return static_file(filename, root='app/static')
# FINAL static routes #########################################################

@app.route('/')
def index(db):
	return template('index')

@app.route('/marcas')
@app.route('/marcas/delete/<id>')
def exibir_marcas(db, error=False, id=False):
	if id:
		try:
			marcas = db.query(Marca).filter(Marca.id == id)[0]
			db.delete(marcas)
			db.commit()
			error=['sucesso', 'Registro gravado com sucesso']
		except BaseException as e:
			error=['erro', e.args[0]]

	marcas = db.query(Marca).all()
	return template('exibir_marcas', marcas=marcas, error=error)

def apagar_marca(db, id):
	try:
		marcas = db.query(Marca).filter(Marca.id == id)[0]
		db.delete(marcas)
		db.commit()
		error=False
	except BaseException as e:
		error=e.args

	marcas = db.query(Marca).all()
	return template('exibir_marcas', marcas=marcas, error=error)

@app.route('/cadastrar_marca', method='POST')
def cadastrar_marca(db):
	from bottle import response
	from json import dumps

	marca = request.forms.get('descricao')
	marca_id = request.forms.get('id')

	if(marca):
		if(marca_id):
			marca = db.query(Marca).filter_by(id=marca_id).update({"descricao": marca})
		else:
			marca = Marca(marca)
			db.add(marca)
		db.commit()
	else:
		response.status = 400
		response.content_type = 'application/json'
		return json.dumps({'error': 'Object already exists with that name'})

	marcas = db.query(Marca).all()

	response.content_type = 'application/json'
	return dumps(marcas, cls=AlchemyEncoder)

@app.route('/produtos')
def exibir_produtos(db):
	produtos = db.query(Produtos).all()
	return template('exibir_produtos', produtos=produtos)

'''
RETORNAR ERRO JSON ############################################################

import json
from bottle import run, route, response

@route('/text')
def get_text():
    response.status = 400
    return 'Object already exists with that name'

@route('/json')
def get_json():
    response.status = 400
    response.content_type = 'application/json'
    return json.dumps({'error': 'Object already exists with that name'})
'''



'''
@app.route('/buscar')
def buscar():
	return template('buscar', produtos=False)

@app.route('/produtos', method="POST")
def acao_buscar(db2):
	from bottle import response
	from json import dumps

	busca = request.forms.get('descricao')

	produtos = db2.query(ProdutosCiss).filter(ProdutosCiss.descricao.like('%'+busca+'%')).all()
	dict = {}
	count = 0
	for p in produtos:
		prod = {}
		prod['id'] = p.id
		prod['descricao'] = p.descricao
		prod['fabricante'] = p.fabricante
		prod['saldo'] = 0
		dict[str(count)] = prod
		count += 1
	response.content_type = 'application/json'
	return dumps(dict)
'''
