from src.domain.game.entity.code import Code
from src.domain.game.entity.game import Game
from src.domain.game.factory.gameFactory import GameFactory
from src.domain.game.repository.gameRepository import GameRepository


class CreateGameService(GameFactory, GameRepository):

    def execute(self, code: Code) -> Game:
        game = super().create(code)

        super().save(game)

        return game
