from repository import Repository

def test_sqlite_reopens_without_reseeding_and_binds_title_safely(tmp_path,monkeypatch):
    monkeypatch.setenv('TASK_DB',str(tmp_path/'tasks.db'))
    repo=Repository();repo.initialize()
    title="Buy milk'); DROP TABLE tasks; --"
    created=repo.create(title);repo.update(created['id'],{'done':True})
    for _ in range(3):
        reopened=Repository();reopened.initialize()
        assert len(reopened.list())==4
        assert reopened.get(created['id'])=={'id':created['id'],'title':title,'done':True}
