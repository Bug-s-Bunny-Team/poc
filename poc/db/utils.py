import os
from typing import Optional

from . import db
from db.models import SocialProfile, PostScore, Post, Location


def init_db(
    user: Optional[str] = None,
    password: Optional[str] = None,
    host: Optional[str] = None,
    database: Optional[str] = None,
):
    db.init(
        user=user if user else os.environ['DB_USER'],
        password=password if password else os.environ['DB_PASSWORD'],
        host=host if host else os.environ['DB_HOST'],
        database=database if database else os.environ['DB_NAME'],
    )
    db.connect()


def create_all_tables():
    db.create_tables(models=[SocialProfile, Location, Post, PostScore])
