import json

from django.http import HttpRequest

from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsRequest import CreateFeedbackByCodeGuessColorsRequest


class DjangoHttpRequestToCreateFeedbackByCodeGuessRequest:
    def transform(self, game_id: int, http_request: HttpRequest) -> CreateFeedbackByCodeGuessColorsRequest:
        return CreateFeedbackByCodeGuessColorsRequest(game_id, self._build_game_code(http_request.body))

    def _build_game_code(self, code_request_param: str) -> [CodePegColor]:
        code_peg_colors = []

        code_peg_values = json.loads(code_request_param)

        for code_peg_value in code_peg_values['code']:
            code_peg_colors.append(CodePegColor(code_peg_value))

        return code_peg_colors
