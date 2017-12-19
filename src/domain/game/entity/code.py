import uuid
from datetime import datetime
from src.domain.game.entity.codePeg import CodePeg


class Code:

    def __init__(self, id: uuid, created_at: datetime, code_pegs: [CodePeg]):
        self._id = id
        self._created_at = created_at
        self.set_code_pegs(code_pegs)

    def set_code_pegs(self, code_pegs):
        self._code_pegs = code_pegs

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def code_pegs(self) -> [CodePeg]:
        return self._code_pegs
