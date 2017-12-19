import uuid

from datetime import datetime

from src.domain.game.factory.gameFactory import GameFactory
from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame


class DjangoGameFactory(GameFactory):
    def create(self, code: DjangoCode) -> DjangoGame:
        return DjangoGame(uuid.uuid4(), datetime.now(), code)
