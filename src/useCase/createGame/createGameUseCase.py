from typing import Any

from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.repository.codePegRepository import CodePegRepository
from src.domain.game.service.createCodeService import CreateCodeService
from src.domain.game.service.createGameService import CreateGameService
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createGame.createGameDataTransformer import CreateGameDataTransformer
from src.useCase.createGame.createGameRequest import CreateGameRequest
from src.useCase.createGame.createGameResponse import CreateGameResponse


class CreateGameUseCase(CodePegRepository, CreateCodeService, CreateGameService, CreateGameDataTransformer):

    def execute(self, request: CreateGameRequest) -> Any:
        code_pegs = self.get_code_pegs(request.code_peg_colors)

        code = CreateCodeService.execute(self, code_pegs)
        game = CreateGameService.execute(self, code)

        return super().transform(CreateGameResponse(game))

    def get_code_pegs(self, code_peg_colors: [CodePegColor]) -> [CodePeg]:
        code_pegs = []
        for code_peg_color in code_peg_colors:
            code_pegs.append(super().find_one_by_color(code_peg_color))

        return code_pegs
