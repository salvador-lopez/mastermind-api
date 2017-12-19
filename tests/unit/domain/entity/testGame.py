import uuid
from unittest import TestCase

from datetime import datetime
from unittest.mock import MagicMock

from src.domain.game.entity.code import Code
from src.domain.game.entity.game import Game


class TestGame(TestCase):
    def test_game_can_be_created(self):
        id = uuid.uuid4()
        created_at = datetime.now()
        code = MagicMock(Code)
        game = Game(id, created_at, code)

        self.assertIs(game.id, id)
        self.assertIs(game.created_at, created_at)
        self.assertIs(game.code, code)
