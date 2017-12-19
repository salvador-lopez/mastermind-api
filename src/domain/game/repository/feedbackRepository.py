import uuid
from abc import ABC, abstractmethod

from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game


class FeedbackRepository(ABC):
    @abstractmethod
    def save(self, feedback: Feedback):
        pass

    @abstractmethod
    def find_all_by_game(self, game: Game) -> [Feedback]:
        pass
