from abc import ABC, abstractmethod

from src.domain.game.entity.feedback import Feedback


class FeedbackFactory(ABC):
    @abstractmethod
    def create(self, black_pegs: int, white_pegs: int) -> Feedback:
        pass
