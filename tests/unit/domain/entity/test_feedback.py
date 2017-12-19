import uuid
from unittest import TestCase

from datetime import datetime

from src.domain.game.entity.feedback import Feedback


class FeedbackTest(TestCase):
    def test_feedback_can_be_created(self):
        id = uuid.uuid4()
        created_at = datetime.now()
        black_pegs = 2
        white_pegs = 1

        feedback = Feedback(id, created_at, black_pegs, white_pegs)

        self.assertIs(feedback.id, id)
        self.assertIs(feedback.black_pegs, black_pegs)
        self.assertIs(feedback.white_pegs, white_pegs)
