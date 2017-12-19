import uuid

from datetime import datetime

from src.domain.game.factory.feedbackFactory import FeedbackFactory
from src.infrastructure.persistence.domain.game.entity.djangoFeedback import DjangoFeedback


class DjangoFeedbackFactory(FeedbackFactory):

    def create(self, black_pegs: int, white_pegs: int) -> DjangoFeedback:
        return DjangoFeedback(uuid.uuid4(), datetime.now(), black_pegs, white_pegs)
