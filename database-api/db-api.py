#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error


def connect(database):
    print(f'connecting to {database}')
    conn = None

    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn


def create_table(conn, name):
    print(f'creating table {name}')
    cur = conn.cursor()

    sql = f'DROP TABLE IF EXISTS {name}'
    cur.execute(sql)
    sql = f"""
        CREATE TABLE {name} (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """
    cur.execute(sql)
    conn.commit()
    cur.close()

    return cur.lastrowid


def insert(conn, name, *args):
    print(f'inserting row {args}')
    cur = conn.cursor()

    sql = f"""
        INSERT INTO {name} (string, number) VALUES (?, ?)
    """
    cur.execute(sql, args)
    conn.commit()
    cur.close()

    return cur.lastrowid


def count_rows(conn):
    cur = conn.cursor()

    sql = "SELECT COUNT(*) FROM test"
    cur.execute(sql)
    conn.commit()
    count = cur.fetchone()[0]
    cur.close()

    return count


def read(conn, name):
    print(f'reading table {name}')
    cur = conn.cursor()
    
    sql = f"SELECT * FROM {name}"
    for row in cur.execute(sql):
        print(row)
    
    conn.commit()
    cur.close()


def drop_table(conn, name):
    print(f'dropping table {name}')
    cur = conn.cursor()

    sql = f"DROP TABLE {name}"
    cur.execute(sql)
    conn.commit()
    cur.close()


def main():
    table_name = 'test'
    database = 'db-api.db'

    conn = connect(database)

    with conn:
        create_table(conn, table_name)

        insert(conn, table_name, 'dog', 1)
        insert(conn, table_name, 'cat', 2)
        insert(conn, table_name, 'bird', 3)

        amount = count_rows(conn)
        print(f'there are {amount} rows in the table.')

        read(conn, table_name)


if __name__ == '__main__':
    main()
