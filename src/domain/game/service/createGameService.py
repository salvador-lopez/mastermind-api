from src.domain.game.entity.code import Code
from src.domain.game.entity.game import Game
from src.domain.game.factory.gameFactory import GameFactory
from src.domain.game.repository.gameRepository import GameRepository


class CreateGameService:
    def __init__(self, game_factory: GameFactory, game_repository: GameRepository):
        self._game_factory = game_factory
        self._game_repository = game_repository

    def execute(self, code: Code) -> Game:
        game = self._game_factory.create(code)

        self._game_repository.save(game)

        return game
