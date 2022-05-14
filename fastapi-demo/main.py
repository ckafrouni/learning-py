import fastapi
import pydantic
import sqlite3

from . import sql_utils


class User(pydantic.BaseModel):
	_id: int
	username: str
	password: str


app = fastapi.FastAPI()
db = 'app.db'

sqlite3.connect('app.db')\
	.execute('CREATE TABLE IF NOT EXISTS user(id integer PRIMARY KEY, username text NOT NULL, password text)')\
	.close()

@app.get("/")
def root():
	return {"hello": "world"}


@app.get("/users/{username}")
def read_user(username: str):
	cur = sql_utils.read(db=db, table='user', key='username', value=repr(username))
	return cur.fetchall()

@app.post("/users")
def create_user(newuser: User):
	sql_utils.insert(db=db, table='user', item=newuser.__dict__)
	return {'msg': 'user added successfully', 'content': newuser.dict()}

