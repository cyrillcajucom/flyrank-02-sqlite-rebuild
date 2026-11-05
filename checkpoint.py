from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 r=c.post('/tasks',json={'title':"Persistent ' quoted"});assert r.status_code==201
 i=r.json()['id'];assert c.post('/tasks',json={}).status_code==400
from repository import Repository
r=Repository();r.initialize();assert r.get(i)['title']=="Persistent ' quoted"
print('PASS insert 201, invalid 400, repository restart persistence and quoted input')
