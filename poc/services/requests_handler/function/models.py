from typing import Optional, Literal

from common.models import LambdaEvent


class Request(LambdaEvent):
    resource: str
    path: str
    httpMethod: Literal['GET', 'POST']
    body: Optional[str] = None

    class Config:
        extra = 'allow'
