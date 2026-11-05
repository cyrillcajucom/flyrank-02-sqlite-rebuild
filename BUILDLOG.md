
## Stage 0
`python checkpoint.py`: PASS automatic table and idempotent three-row seed

## Stage 1
`python checkpoint.py`: PASS reads from SQLite, missing 404

## Stage 2
`python checkpoint.py`: PASS insert 201, invalid 400, repository restart persistence and quoted input

## Stage 3
`python checkpoint.py`: PASS full CRUD: 200/201/204/400/404

## Stage 4
`python checkpoint.py`: PASS SELECT and SQL UPDATE visible immediately through API; DB Browser screenshot pending

## Stage 5
`python checkpoint.py`: PASS full CRUD: 200/201/204/400/404
PASS clean database auto-creation and persistence after restart

## Additional validation
Original endpoint regression tests reused unchanged: `python -m pytest -q`
...                                                                      [100%]
3 passed in 1.30s

