from abc import ABC, abstractmethod
from typing import Optional

import boto3


class SessionProvider(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_session(self, username: str) -> dict:
        pass

    @abstractmethod
    def refresh_session(self, username: str, session_data: dict):
        pass


class InstagramSessionProvider(SessionProvider):
    def __init__(self, table_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dynamodb = boto3.resource('dynamodb')
        self._table = self._dynamodb.Table(table_name)

    def get_session(self, username: str) -> Optional[dict]:
        session = self._table.get_item(Key={'username': username}).get('Item')
        if session:
            return session.get('session_data')
        return None

    def refresh_session(self, username: str, session_data: dict):
        self._table.update_item(
            Key={'username': username},
            UpdateExpression='SET session_data = :s',
            ExpressionAttributeValues={':s': session_data}
        )
