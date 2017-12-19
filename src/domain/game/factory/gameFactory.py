from abc import ABC, abstractmethod

from src.domain.game.entity.game import Game
from src.domain.game.entity.code import Code


class GameFactory(ABC):
    @abstractmethod
    def create(self, code: Code) -> Game:
        pass
