import uuid
from unittest import TestCase
from unittest.mock import MagicMock
from datetime import datetime

from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg


class CodeTest(TestCase):
    def test_code_can_be_created(self):
        id = uuid.uuid4()
        created_at = datetime.now()
        code_pegs = [MagicMock(CodePeg)]
        code = Code(id, created_at, code_pegs)

        self.assertIs(code.id, id)
        self.assertIs(code.created_at, created_at)
        self.assertIs(code.code_pegs, code_pegs)
