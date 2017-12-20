from src.infrastructure.dependencyInjection.staticFactories.domainServices import \
    CreateFeedbackByCodeGuessServiceStaticFactory, CreateCodeServiceStaticFactory, CreateGameServiceStaticFactory, \
    CreateHistoricEntryServiceStaticFactory
from src.infrastructure.dependencyInjection.staticFactories.repositories import DjangoCodePegRepositoryStaticFactory, \
    DjangoGameRepositoryStaticFactory, DjangoCodeRepositoryStaticFactory, DjangoHistoricEntryRepositoryStaticFactory
from src.infrastructure.dependencyInjection.staticFactories.responseDataTransformers import \
    CreateGameResponseToApiResourceDictionaryStaticFactory, \
    CreateFeedbackByCodeGuessResponseToApiResourceDictionaryStaticFactory, \
    GetHistoricByGameIdToApiResourceDictionaryStaticFactory
from src.useCase.createGame.createGameUseCase import CreateGameUseCase
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsUseCase import CreateFeedbackByCodeGuessColorsUseCase
from src.useCase.getHistoric.getHistoricByGameIdUseCase import GetHistoricByGameIdUseCase


class CreateGameUseCaseStaticFactory:
    @staticmethod
    def create() -> CreateGameUseCase:
        return CreateGameUseCase(
            DjangoCodePegRepositoryStaticFactory.create(),
            CreateCodeServiceStaticFactory.create(),
            CreateGameServiceStaticFactory.create(),
            CreateGameResponseToApiResourceDictionaryStaticFactory.create()
        )


class CreateFeedbackByCodeGuessColorsUseCaseStaticFactory:
    @staticmethod
    def create() -> CreateFeedbackByCodeGuessColorsUseCase:
        return CreateFeedbackByCodeGuessColorsUseCase(
            DjangoGameRepositoryStaticFactory.create(),
            CreateFeedbackByCodeGuessServiceStaticFactory.create(),
            CreateHistoricEntryServiceStaticFactory.create(),
            DjangoCodeRepositoryStaticFactory.create(),
            CreateFeedbackByCodeGuessResponseToApiResourceDictionaryStaticFactory.create()
        )


class GetHistoricByGameIdUseCaseStaticFactory:
    @staticmethod
    def create() -> GetHistoricByGameIdUseCase:
        return GetHistoricByGameIdUseCase(
            DjangoGameRepositoryStaticFactory.create(),
            DjangoHistoricEntryRepositoryStaticFactory.create(),
            GetHistoricByGameIdToApiResourceDictionaryStaticFactory.create()
        )
