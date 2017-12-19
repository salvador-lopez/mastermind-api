import uuid
from abc import ABC, abstractmethod

from src.domain.game.entity.game import Game
from src.domain.game.entity.historicEntry import HistoricEntry
from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback


class HistoricEntryFactory(ABC):
    @abstractmethod
    def create(self, game: Game, code_guess: Code, feedback: Feedback) -> HistoricEntry:
        pass
