import uuid

from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.valueObject.codePegColor import CodePegColor


class TestableCodePeg(CodePeg):
    def __init__(self, id: uuid, color: CodePegColor):
        self._id = id
        self._color = color
