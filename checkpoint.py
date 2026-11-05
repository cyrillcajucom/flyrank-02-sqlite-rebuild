from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 import sqlite3
 with sqlite3.connect('tasks.db') as d:
  assert len(d.execute('SELECT * FROM tasks').fetchall())>=3
  d.execute('UPDATE tasks SET done=1 WHERE id=1')
 assert c.get('/tasks/1').json()['done'] is True
 print('PASS SELECT and SQL UPDATE visible immediately through API; DB Browser screenshot pending')
