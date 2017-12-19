from unittest import TestCase
from unittest.mock import Mock

from src.domain.game.entity.code import Code
from src.domain.game.entity.game import Game
from src.domain.game.factory.gameFactory import GameFactory
from src.domain.game.repository.codeRepository import CodeRepository
from src.domain.game.service.createGameService import CreateGameService


class TestCreateGameService(TestCase):
    def test_will_create_and_save_and_return_game_as_expected(self):
        game_factory_mock = Mock(GameFactory)
        game_expected = Mock(Game)
        game_factory_mock.configure_mock(**{'create.return_value': game_expected})
        game_repository_mock = Mock(CodeRepository)

        create_game_service = CreateGameService(game_factory_mock, game_repository_mock)
        code_mock = Mock(Code)
        game = create_game_service.execute(code_mock)

        game_repository_mock.save.assert_called_once_with(game_expected)
        self.assertIs(game_expected, game)
