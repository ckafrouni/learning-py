#!/usr/bin/python3 #-i
import sqlite3
from employee import (
    Employee, 
    insert_emp, 
    get_emps, 
    update_pay, 
    remove_emp,
    parseEmployees
)

#------Setup Database-------#
conn = sqlite3.connect('employee.db')
#conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employees' ''')
res = cur.fetchone()[0]
EXIST = res == 1

#if the count is 1, then table exists
if EXIST : 
	print('Table exists.')
else :
    cur.execute("""CREATE TABLE employees (
        first text, last text, pay integer )""")
    print('Table does not exist.')


#-----Create Employee-----#

if EXIST:
    get_emps(cur)
else:
    parser = parseEmployees('emps.json')
    for emp in parser:
        insert_emp(emp, conn, cur)

#-----testing-------------#

#breakpoint()
conn.close()