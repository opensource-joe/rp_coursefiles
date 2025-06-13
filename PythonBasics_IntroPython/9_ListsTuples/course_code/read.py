# read.py
"""Reads and displays data from a SQLite database."""

import sqlite3

with sqlite3.connect("company.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")

    # Fetch one row - this will be a tuple
    row = cursor.fetchone()
    print(row)  # (1, 'Adisa', 'Software Engineer')
    print(type(row))  # <class 'tuple'>

    # Unpack the values
    employee_id, name, role = row
    print(name)  # Adisa
    print(role)  # Software Engineer
