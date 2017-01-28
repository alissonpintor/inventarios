import bottle_session
from bottle import Bottle, TEMPLATE_PATH
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)
engineDb2 = create_engine("db2+ibm_db://dba:overhead@192.168.104.3:50000/STOKY", echo=True)

app = Bottle()
TEMPLATE_PATH.insert(0, 'app/views/')
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

pluginDb2 = sqlalchemy.Plugin(
    engineDb2,
    Base.metadata,
    keyword='db2',
    create=True,
    commit=True,
    use_kwargs=False
)

plugin_session = bottle_session.SessionPlugin(cookie_lifetime=10)

app.install(plugin)
app.install(pluginDb2)
app.install(plugin_session)

from app.controllers import default
from app.models import tables
