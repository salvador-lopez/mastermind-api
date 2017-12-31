from src.domain.game.service.createCodeService import CreateCodeService
from src.infrastructure.persistence.domain.game.factory.djangoCodeFactory import DjangoCodeFactory
from src.infrastructure.persistence.domain.game.repository.djangoCodeRepository import DjangoCodeRepository


class ClientCreateCodeService(CreateCodeService, DjangoCodeFactory, DjangoCodeRepository):
    pass
