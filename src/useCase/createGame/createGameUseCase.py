from typing import Any

from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.repository.codePegRepository import CodePegRepository
from src.domain.game.service.createCodeService import CreateCodeService
from src.domain.game.service.createGameService import CreateGameService
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createGame.createGameDataTransformer import CreateGameDataTransformer
from src.useCase.createGame.createGameRequest import CreateGameRequest
from src.useCase.createGame.createGameResponse import CreateGameResponse


class CreateGameUseCase:

    def __init__(
            self,
            code_peg_repository: CodePegRepository,
            create_code_service: CreateCodeService,
            create_game_service: CreateGameService,
            data_transformer: CreateGameDataTransformer
    ):
        self._code_peg_repository = code_peg_repository
        self._create_code_service = create_code_service
        self._create_game_service = create_game_service
        self._data_transformer = data_transformer

    def execute(self, request: CreateGameRequest) -> Any:
        code_pegs = self.get_code_pegs(request.code_peg_colors)

        code = self._create_code_service.execute(code_pegs)
        game = self._create_game_service.execute(code)

        return self._data_transformer.transform(CreateGameResponse(game))

    def get_code_pegs(self, code_peg_colors: [CodePegColor]) -> [CodePeg]:
        code_pegs = []
        for code_peg_color in code_peg_colors:
            code_pegs.append(self._code_peg_repository.find_one_by_color(code_peg_color))

        return code_pegs
