from unittest import TestCase

from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.entity.game import Game
from src.domain.game.repository.codePegRepository import CodePegRepository
from src.domain.game.service.createCodeService import CreateCodeService
from src.domain.game.service.createGameService import CreateGameService
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createGame.createGameDataTransformer import CreateGameDataTransformer
from src.useCase.createGame.createGameRequest import CreateGameRequest
from src.useCase.createGame.createGameResponse import CreateGameResponse
from src.useCase.createGame.createGameUseCase import CreateGameUseCase
from unittest.mock import Mock


class TestCreateGameUseCase(TestCase):
    def test_create_a_game_and_return_the_transformed_response_as_expected(self):
        code_peg_repository_mock = Mock(CodePegRepository)
        code_peg_mock = Mock(CodePeg)
        code_peg_repository_mock.configure_mock(**{'find_one_by_color.return_value': code_peg_mock})

        create_code_service_mock = Mock(CreateCodeService)
        code_mock = Mock(Code)
        create_code_service_mock.configure_mock(**{'execute.return_value': code_mock})

        create_game_service_mock = Mock(CreateGameService)
        game_mock = Mock(Game)
        create_game_service_mock.configure_mock(**{'execute.return_value': game_mock})

        data_transformer_mock = Mock(CreateGameDataTransformer)
        response_expected = CreateGameResponse(game_mock)
        data_transformer_mock.configure_mock(**{'transform.return_value': response_expected})

        use_case = CreateGameUseCase(
            code_peg_repository_mock,
            create_code_service_mock,
            create_game_service_mock,
            data_transformer_mock
        )
        code_peg_color = CodePegColor('RED')
        code_peg_colors = [code_peg_color, code_peg_color, code_peg_color, code_peg_color]

        request = CreateGameRequest(code_peg_colors)

        response = use_case.execute(request)

        code_peg_repository_mock.find_one_by_color.assert_called_with(code_peg_color)
        self.assertEqual(code_peg_repository_mock.find_one_by_color.call_count, 4)

        code_peg_mocks = [code_peg_mock, code_peg_mock, code_peg_mock, code_peg_mock]
        create_code_service_mock.execute.assert_called_once_with(code_peg_mocks)

        create_game_service_mock.execute.assert_called_once_with(code_mock)

        self.assertEqual(response, response_expected)
