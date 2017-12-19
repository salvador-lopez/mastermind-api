from src.domain.game.valueObject.codePegColor import CodePegColor


class CreateGameRequest:

    def __init__(self, code_peg_colors: [CodePegColor]):
        self._code_peg_colors = code_peg_colors

    @property
    def code_peg_colors(self) -> [CodePegColor]:
        return self._code_peg_colors
