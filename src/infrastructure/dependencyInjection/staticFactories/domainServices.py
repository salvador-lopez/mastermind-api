from src.domain.game.service.createCodeService import CreateCodeService
from src.domain.game.service.createFeedbackByCodeGuessColorsService import CreateFeedbackByCodeGuessColorsService
from src.domain.game.service.createHistoricEntryService import CreateHistoricEntryService
from src.domain.game.service.createGameService import CreateGameService
from src.infrastructure.dependencyInjection.staticFactories.abstractFactories import DjangoCodeFactoryStaticFactory, \
    DjangoGameFactoryStaticFactory, DjangoHistoricEntryFactoryStaticFactory, DjangoFeedbackFactoryStaticFactory
from src.infrastructure.dependencyInjection.staticFactories.repositories import DjangoGameRepositoryStaticFactory, \
    DjangoCodeRepositoryStaticFactory, DjangoHistoricEntryRepositoryStaticFactory, DjangoFeedbackRepositoryStaticFactory


class CreateCodeServiceStaticFactory:
    @staticmethod
    def create() -> CreateCodeService:
        return CreateCodeService(
            DjangoCodeFactoryStaticFactory.create(),
            DjangoCodeRepositoryStaticFactory.create()
        )


class CreateGameServiceStaticFactory:
    @staticmethod
    def create() -> CreateGameService:
        return CreateGameService(
            DjangoGameFactoryStaticFactory.create(),
            DjangoGameRepositoryStaticFactory.create()
        )


class CreateFeedbackByCodeGuessServiceStaticFactory:
    @staticmethod
    def create() -> CreateFeedbackByCodeGuessColorsService:
        return CreateFeedbackByCodeGuessColorsService(
            DjangoFeedbackFactoryStaticFactory.create(),
            DjangoFeedbackRepositoryStaticFactory.create()
        )


class CreateHistoricEntryServiceStaticFactory:
    @staticmethod
    def create() -> CreateHistoricEntryService:
        return CreateHistoricEntryService(
            DjangoHistoricEntryFactoryStaticFactory.create(),
            DjangoHistoricEntryRepositoryStaticFactory.create()
        )
