from src.domain.game.entity.feedback import Feedback


class CreateFeedbackByCodeGuessColorsResponse:

    def __init__(self, feedback: Feedback):
        self._feedback = feedback

    @property
    def feedback(self) -> Feedback:
        return self._feedback
