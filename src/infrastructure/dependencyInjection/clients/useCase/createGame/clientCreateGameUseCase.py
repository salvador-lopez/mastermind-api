from src.infrastructure.dependencyInjection.clients.domain.game.service.clientCreateCodeService import \
    ClientCreateCodeService
from src.infrastructure.dependencyInjection.clients.domain.game.service.clientCreateGameService import \
    ClientCreateGameService
from src.infrastructure.persistence.domain.game.repository.djangoCodePegRepository import DjangoCodePegRepository
from src.infrastructure.presentation.dataTransformation.createGame.createGameResponseToApiResourceDictionary import \
    CreateGameResponseToApiResourceDictionary
from src.useCase.createGame.createGameUseCase import CreateGameUseCase


class ClientCreateGameUseCase(CreateGameUseCase, DjangoCodePegRepository, ClientCreateCodeService,
                              ClientCreateGameService, CreateGameResponseToApiResourceDictionary):
    pass
