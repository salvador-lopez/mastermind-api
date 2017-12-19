import uuid
from unittest import TestCase

from unittest.mock import MagicMock

from src.domain.game.valueObject.codePegColor import CodePegColor
from tests.unit.domain.entity.testableCodePeg import TestableCodePeg


class CodePegTest(TestCase):
    def test_code_peg_can_be_created(self):
        id = uuid.uuid4()
        color = MagicMock(CodePegColor)
        code_peg = TestableCodePeg(id, color)

        self.assertIs(code_peg.id, id)
        self.assertIs(code_peg.color, color)
