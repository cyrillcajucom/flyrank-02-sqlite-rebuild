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
