from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 t=c.post('/tasks',json={'title':'Checkpoint'}); assert t.status_code==201
 i=t.json()['id']; assert c.get('/tasks/'+str(i)).status_code==200
 assert c.put('/tasks/'+str(i),json={'done':True}).json()['done'] is True
 assert c.put('/tasks/'+str(i),json={'title':''}).status_code==400
 assert c.delete('/tasks/'+str(i)).status_code==204
 for method in ['get','put','delete']:
  kwargs={'json':{'title':'missing'}} if method=='put' else {}
  r=getattr(c,method)('/tasks/999',**kwargs); assert r.status_code==404 and 'error' in r.json()
 print('PASS full CRUD: 200/201/204/400/404')

import os,tempfile,sqlite3
from repository import Repository
with tempfile.TemporaryDirectory() as d:
 os.environ['TASK_DB']=d+'/clean.db';r=Repository();r.initialize();r.initialize();assert len(r.list())==3
 t=r.create('survives restart');r=Repository();r.initialize();assert r.get(t['id'])['title']=='survives restart'
print('PASS clean database auto-creation and persistence after restart')
