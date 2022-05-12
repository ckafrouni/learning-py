import functools
import sqlite3
import contextlib
from typing import Any, Callable, List, Tuple

@contextlib.contextmanager
def sqlite_connection(db: str):
	conn = None
	try:
		conn = sqlite3.connect(db)
		print(f'Connection to {db} established.\n{"":->40}')
		yield conn
	finally:
		if conn:
			print(f'{"":->40}\nClosing connection to {db}')
			conn.close()

def sql_exec(func: Callable[[Any], str]):
	@functools.wraps(func)
	def wrapper(conn: sqlite3.Connection, table: str, *args, **kwargs):
		cur = conn.cursor()
		cur.execute(func(table, *args, **kwargs))
		conn.commit()
		return cur
	return wrapper

@sql_exec
def create_table(table: str, columns: List[str]) -> str:
	cols_str = ",".join(columns)
	return f'CREATE TABLE IF NOT EXISTS {table} ({cols_str});'

@sql_exec
def insert_item(table: str, **values) -> str:
	ks = ','.join(k for k in values.keys())
	vs = ','.join(v for v in values.values())
	return f'INSERT INTO {table}({ks}) VALUES({vs})'

@sql_exec
def update_item(table: str, pk: Tuple[str, str], **values) -> str:
	updates_str = ','.join([f'{k} = {v}' for k, v in values.items()])
	return f'UPDATE {table} SET {updates_str} WHERE {pk[0]} = {pk[1]};'

@sql_exec
def select_items(table: str, pk: Tuple[str, str]) -> str:
	return f'SELECT * FROM {table} WHERE {pk[0]} = {pk[1]};'

def print_selected_items(items: List[Tuple[Any]]) -> None:
	print(f"SELECTION:\n\t{'-'.join(str(row) for row in items)}")
