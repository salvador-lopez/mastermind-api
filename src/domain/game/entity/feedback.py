import uuid

from datetime import datetime


class Feedback:

    def __init__(self, id: uuid , created_at: datetime, black_pegs, white_pegs):
        self._id = id
        self._created_at = created_at
        self._black_pegs = black_pegs
        self._white_pegs = white_pegs

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def black_pegs(self) -> int:
        return self._black_pegs

    @property
    def white_pegs(self) -> int:
        return self._white_pegs
