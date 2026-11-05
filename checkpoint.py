from repository import Repository
import sqlite3
r=Repository();r.initialize();r.initialize()
with sqlite3.connect('tasks.db') as d: assert d.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]==3
print('PASS automatic table and idempotent three-row seed')
