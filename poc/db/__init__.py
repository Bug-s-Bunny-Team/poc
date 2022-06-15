import os
from typing import Optional

from pony.orm import Database

db = Database()


def init_db(
    user: Optional[str] = None,
    password: Optional[str] = None,
    host: Optional[str] = None,
    database: Optional[str] = None,
):
    db.bind(
        provider='postgres',
        user=user if user else os.environ['DB_USER'],
        password=password if password else os.environ['DB_PASSWORD'],
        host=host if host else os.environ['DB_HOST'],
        database=database if database else os.environ['DB_NAME'],
    )
    db.generate_mapping()
