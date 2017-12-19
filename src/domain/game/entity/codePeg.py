import uuid
from src.domain.game.valueObject.codePegColor import CodePegColor


class CodePeg:
    _id = uuid
    _color = CodePegColor

    @property
    def id(self) -> uuid:
        return self._id

    @property
    def color(self) -> CodePegColor:
        return self._color
