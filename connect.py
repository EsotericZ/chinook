import sqlite3
import pandas as pd

def run_query(q):
    with sqlite3.connect('chinook.db') as conn:
        return pd.read_sql_query(q, conn)

def run_command(c):
    with sqlite3.connect('chinook.db') as conn:
        conn.isolation_level = None
        conn.execute(c)

def show_tables():
    q = "SELECT * FROM sqlite_master WHERE type = 'table'"
    return run_query(q)

# print(show_tables())
