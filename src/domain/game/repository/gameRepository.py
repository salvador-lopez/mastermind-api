import uuid
from abc import ABC, abstractmethod

from src.domain.game.entity.game import Game


class GameRepository(ABC):
    @abstractmethod
    def save(self, game: Game):
        pass

    @abstractmethod
    def find_one_by_id(self, game_id: uuid) -> Game:
        """
        :raise: GameNotFoundException
        """
