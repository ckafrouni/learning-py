import sqlite3
from typing import Any


def insert(db: str, table: str, item: dict[str,Any]) -> sqlite3.Cursor:
	columns = ','.join(item.keys())
	place_holder = ','.join('?' for _ in item.keys())
	with sqlite3.connect(db) as conn:
		cur = conn.cursor()
		cur.execute(f'INSERT INTO {table}({columns}) VALUES({place_holder})', tuple(item.values()))
		conn.commit()
		return cur

def read(db: str, table: str, key: str, value: Any) -> sqlite3.Cursor:
	with sqlite3.connect(db) as conn:
		cur = conn.cursor()
		cur.execute(f'SELECT * FROM {table} WHERE ? = ?;', (key, value))
		conn.commit()
		return cur