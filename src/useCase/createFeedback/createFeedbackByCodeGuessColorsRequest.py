import uuid

from src.domain.game.valueObject.codePegColor import CodePegColor


class CreateFeedbackByCodeGuessColorsRequest:

    def __init__(self, game_id, colors: [CodePegColor]):
        self._game_id = game_id
        self._colors = colors

    @property
    def game_id(self) -> uuid:
        return self._game_id

    @property
    def colors(self) -> [CodePegColor]:
        return self._colors
