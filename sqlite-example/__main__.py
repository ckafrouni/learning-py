from . import sqlite_utils as foo


def main(db: str=':memory:') -> None:
	with foo.sqlite_connection(db) as conn:
		table = 'employee'
		foo.create_table(conn, table, [
			'id integer PRIMARY KEY',
			'firstname text NOT NULL',
			'lastname text NOT NULL',
		])

		foo.insert_item(conn, table, firstname="'chris'", 	lastname="'kafrouni'")
		foo.insert_item(conn, table, firstname="'fonzi'",	lastname="'karam'")
		foo.insert_item(conn, table, firstname="'john'",	lastname="'doe'")
		foo.insert_item(conn, table, firstname="'fonzi'", 	lastname="'brown'")

		foo.update_item(conn, table, pk=('id', 3), firstname="'Tarazan'")

		cur = foo.select_items(conn, table, pk=('id', 3))
		foo.print_selected_items(cur.fetchall())

		cur = foo.select_items(conn, table, pk=('firstname', "'fonzi'"))
		foo.print_selected_items(cur.fetchall())

if __name__ == '__main__':
	# main('./employee.db')
	main() # in memory