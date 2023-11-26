import sqlite3
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()
    

SQLITE_PATH = Path('./db.sqlite')


def sqlite_extractor(table_name):       
    with conn_context(SQLITE_PATH) as conn:
        curs = conn.cursor()
        curs.execute(f"""
        SELECT * FROM {table_name};
        """)
        data = curs.fetchall()
    return data