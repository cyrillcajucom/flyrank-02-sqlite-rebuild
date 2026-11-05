# SQLite task API rebuild

AI-assisted rebuild from flyrank-02-sqlite and the new A1 rebuild. This is not hand-written original coursework. Real current-time stage checkpoints are in BUILDLOG.md.

SQLite persists data in a local file without a separate server, which suits this small API. Unlike A1, a restart retains tasks. Parameterized queries treat user input as data.

Install Python 3.12+, then `python -m pip install -r requirements.txt`.
Run: `python -m uvicorn app:app --port 8102`. Database, table and exactly three examples are created automatically on the first run. Optional TASK_DB sets another file path.

| Method | Endpoint | Result |
|---|---|---|
| GET | /tasks, /tasks/{id} | 200; 404 missing |
| POST | /tasks | 201; 400 invalid |
| PUT | /tasks/{id} | 200; 400 invalid; 404 missing |
| DELETE | /tasks/{id} | 204; 404 missing |

Example SQL: `SELECT * FROM tasks WHERE done = 0;` returns incomplete tasks. `explore.sql` contains direct exploration statements. Stage 4 checked that direct SQL changes are visible immediately via the API.

## Requirement checks
- [x] Same API and unchanged A1 CRUD checkpoint pass on SQLite.
- [x] Automatic file/table creation; exactly three seeds, no duplication on restart.
- [x] Parameterized SQL for CRUD, with 200/201/204/400/404 and JSON errors.
- [x] Persistence verified by reopening repository after create.
- [ ] New DB Browser screenshot and visual persistence verification pending.
- [x] Public repo with six current-time stage commits and setup/query explanation.

Passing the same endpoint checkpoint across storage implementations demonstrates that clients depend on the API contract, not the storage engine. Authorship is AI-assisted as authorized by the user.
