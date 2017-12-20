import json
from django.http import HttpRequest

from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createGame.createGameRequest import CreateGameRequest


class DjangoHttpRequestToCreateGameRequest:
    def transform(self, http_request: HttpRequest) -> CreateGameRequest:
        return CreateGameRequest(self._build_code_peg_colors(http_request.body))

    def _build_code_peg_colors(self, code_request_param: str) -> [CodePegColor]:
        code_peg_colors = []

        code_peg_color_values = json.loads(code_request_param)

        for code_peg_color_value in code_peg_color_values['code']:
            code_peg_colors.append(CodePegColor(code_peg_color_value))

        return code_peg_colors
