from repository import Repository

def test_existing_rows_are_not_seeded_again(tmp_path,monkeypatch):
    monkeypatch.setenv('TASK_DB',str(tmp_path/'tasks.db'))
    repo=Repository()
    with repo.connect() as db:
        db.execute('CREATE TABLE tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,done INTEGER NOT NULL DEFAULT 0)')
        db.execute("INSERT INTO tasks(title) VALUES ('existing')")
    repo.initialize()
    assert [t['title'] for t in repo.list()]==['existing']
