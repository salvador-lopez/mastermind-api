import uuid
from unittest import TestCase

from datetime import datetime
from unittest.mock import MagicMock

from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game
from src.domain.game.entity.historicEntry import HistoricEntry


class TestHistoricEntry(TestCase):
    def test_game_can_be_created(self):
        id = uuid.uuid4()
        created_at = datetime.now()
        game = MagicMock(Game)
        code_guess = MagicMock(Code)
        feedback = MagicMock(Feedback)

        historic_entry = HistoricEntry(id, created_at, game, code_guess, feedback)

        self.assertIs(historic_entry.id, id)
        self.assertIs(historic_entry.created_at, created_at)
        self.assertIs(historic_entry.game, game)
        self.assertIs(historic_entry.code_guess, code_guess)
        self.assertIs(historic_entry.game_feedback, feedback)
