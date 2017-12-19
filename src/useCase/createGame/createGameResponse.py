from src.domain.game.entity.game import Game


class CreateGameResponse:
    def __init__(self, game: Game):
        self._game = game

    @property
    def game(self) -> Game:
        return self._game
