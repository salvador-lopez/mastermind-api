from src.infrastructure.persistence.domain.game.repository.djangoCodePegRepository import DjangoCodePegRepository
from src.infrastructure.persistence.domain.game.repository.djangoCodeRepository import DjangoCodeRepository
from src.infrastructure.persistence.domain.game.repository.djangoFeedbackRepository import DjangoFeedbackRepository
from src.infrastructure.persistence.domain.game.repository.djangoGameRepository import DjangoGameRepository
from src.infrastructure.persistence.domain.game.repository.djangoHistoricEntryRepository import \
    DjangoHistoricEntryRepository


class DjangoCodePegRepositoryStaticFactory:
    @staticmethod
    def create() -> DjangoCodePegRepository:
        return DjangoCodePegRepository()


class DjangoCodeRepositoryStaticFactory:
    @staticmethod
    def create() -> DjangoCodeRepository:
        return DjangoCodeRepository()


class DjangoGameRepositoryStaticFactory:
    @staticmethod
    def create() -> DjangoGameRepository:
        return DjangoGameRepository()


class DjangoFeedbackRepositoryStaticFactory:
    @staticmethod
    def create() -> DjangoFeedbackRepository:
        return DjangoFeedbackRepository()


class DjangoHistoricEntryRepositoryStaticFactory:
    @staticmethod
    def create() -> DjangoHistoricEntryRepository:
        return DjangoHistoricEntryRepository()
