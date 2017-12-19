import uuid

from datetime import datetime

from src.domain.game.entity.code import Code


class Game:

    def __init__(self, id: uuid, created_at: datetime, code: Code):
        self._id = id
        self._created_at = created_at
        self._code = code

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def code(self) -> Code:
        return self._code
