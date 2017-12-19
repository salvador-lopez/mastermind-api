import uuid


class GameNotFoundException(Exception):
    def __init__(self, game_id: uuid):
        self.message = 'Game not found for this id: ' + game_id
