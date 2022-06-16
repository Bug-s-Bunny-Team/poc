from db.utils import init_db, create_all_tables


def test_connect():
    init_db('user', 'password', '172.18.0.10', 'poc')
    create_all_tables()

