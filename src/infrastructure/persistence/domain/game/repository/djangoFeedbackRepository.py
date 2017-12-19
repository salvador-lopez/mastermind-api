from src.domain.game.repository.feedbackRepository import FeedbackRepository
from src.infrastructure.persistence.domain.game.entity.djangoFeedback import DjangoFeedback
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame


class DjangoFeedbackRepository(FeedbackRepository):
    def save(self, feedback: DjangoFeedback):
        DjangoFeedback.save(feedback)

    def find_all_by_game(self, game: DjangoGame) -> [DjangoFeedback]:
        return DjangoFeedback.objects.filter(_game=game)
