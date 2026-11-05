import os
import sqlite3
from contextlib import contextmanager

class Repository:
    @contextmanager
    def connect(self):
        db = sqlite3.connect(os.getenv("TASK_DB", "tasks.db"))
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def initialize(self):
        with self.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)")
            db.execute("CREATE TABLE IF NOT EXISTS initialization (id INTEGER PRIMARY KEY)")
            if not db.execute("SELECT id FROM initialization WHERE id = 1").fetchone():
                if not db.execute('SELECT 1 FROM tasks LIMIT 1').fetchone():
                    db.executemany("INSERT INTO tasks (title) VALUES (?)", [("Learn APIs",), ("Read a book",), ("Take a walk",)])
                db.execute("INSERT INTO initialization VALUES (1)")

    def convert(self, row): return {"id": row["id"], "title": row["title"], "done": bool(row["done"])} if row else None

