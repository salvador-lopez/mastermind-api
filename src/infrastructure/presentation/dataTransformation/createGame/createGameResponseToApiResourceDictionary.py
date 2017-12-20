from src.useCase.createGame.createGameDataTransformer import CreateGameDataTransformer
from src.useCase.createGame.createGameResponse import CreateGameResponse


class CreateGameResponseToApiResourceDictionary(CreateGameDataTransformer):

    def transform(self, create_game_response: CreateGameResponse) -> dict:
        return {'id': create_game_response.game.id}
