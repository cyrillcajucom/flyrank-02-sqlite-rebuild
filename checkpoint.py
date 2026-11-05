from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 assert len(c.get("/tasks").json())==3
 assert c.get("/tasks/1").status_code==200
 assert c.get("/tasks/999").status_code==404
 print("PASS reads from SQLite, missing 404")
