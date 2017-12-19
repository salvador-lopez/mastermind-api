import uuid
from datetime import datetime

from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game


class HistoricEntry:

    def __init__(self, id: uuid, created_at: datetime, game: Game, code_guess: Code, game_feedback: Feedback):
        self._id = id
        self._created_at = created_at
        self._game = game
        self._code_guess = code_guess
        self._game_feedback = game_feedback

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def game(self) -> Game:
        return self._game

    @property
    def code_guess(self) -> Code:
        return self._code_guess

    @property
    def game_feedback(self) -> Feedback:
        return self._game_feedback
