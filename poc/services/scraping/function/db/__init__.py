import os

from pony.orm import Database

db = Database()


def init_db():
    db.bind(
        provider='postgres',
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
    )
    db.generate_mapping()
