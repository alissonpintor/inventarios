import bcrypt
from app import app
from app.models.tables import Produtos
from app.models.sql import ProdutosCiss
from bottle import template, static_file, request, redirect

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
def index(db2):
	produtos = db2.query(ProdutosCiss).all()
	return template('inventario', produtos=produtos)



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
