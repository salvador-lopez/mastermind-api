from src.infrastructure.persistence.domain.game.factory.djangoCodeFactory import DjangoCodeFactory
from src.infrastructure.persistence.domain.game.factory.djangoFeedbackFactory import DjangoFeedbackFactory
from src.infrastructure.persistence.domain.game.factory.djangoGameFactory import DjangoGameFactory
from src.infrastructure.persistence.domain.game.factory.djangoHistoricEntryFactory import DjangoHistoricEntryFactory


class DjangoCodeFactoryStaticFactory:
    @staticmethod
    def create() -> DjangoCodeFactory:
        return DjangoCodeFactory()


class DjangoGameFactoryStaticFactory:
    @staticmethod
    def create() -> DjangoGameFactory:
        return DjangoGameFactory()


class DjangoFeedbackFactoryStaticFactory:
    @staticmethod
    def create() -> DjangoFeedbackFactory:
        return DjangoFeedbackFactory()


class DjangoHistoricEntryFactoryStaticFactory:
    @staticmethod
    def create() -> DjangoHistoricEntryFactory:
        return DjangoHistoricEntryFactory()
