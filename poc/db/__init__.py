import os
from typing import Optional

from peewee import PostgresqlDatabase, DatabaseProxy

db = DatabaseProxy()


def init_db(
    user: Optional[str] = None,
    password: Optional[str] = None,
    host: Optional[str] = None,
    database: Optional[str] = None,
):
    postgres = PostgresqlDatabase(
        user=user if user else os.environ['DB_USER'],
        password=password if password else os.environ['DB_PASSWORD'],
        host=host if host else os.environ['DB_HOST'],
        database=database if database else os.environ['DB_NAME'],
    )
    db.initialize(postgres)
