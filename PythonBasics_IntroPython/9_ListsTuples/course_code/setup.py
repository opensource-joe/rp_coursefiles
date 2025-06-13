# setup.py
"""
Creates a database with an 'employees' table
and one record.
"""

import sqlite3

with sqlite3.connect("company.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT
        )
    """
    )
    cursor.execute(
        """
        INSERT INTO employees (id, name, role)
        VALUES (?, ?, ?)
    """,
        (1, "Adisa", "Software Engineer"),
    )
    connection.commit()
