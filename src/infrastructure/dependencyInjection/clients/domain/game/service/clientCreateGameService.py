from src.domain.game.service.createGameService import CreateGameService
from src.infrastructure.persistence.domain.game.factory.djangoGameFactory import DjangoGameFactory
from src.infrastructure.persistence.domain.game.repository.djangoGameRepository import DjangoGameRepository


class ClientCreateGameService(CreateGameService, DjangoGameFactory, DjangoGameRepository):
    pass
