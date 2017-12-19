import uuid

from datetime import datetime

from src.domain.game.factory.historicEntryFactory import HistoricEntryFactory
from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode
from src.infrastructure.persistence.domain.game.entity.djangoFeedback import DjangoFeedback
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame
from src.infrastructure.persistence.domain.game.entity.djangoHistoricEntry import DjangoHistoricEntry


class DjangoHistoricEntryFactory(HistoricEntryFactory):
    def create(self, game: DjangoGame, code_guess: DjangoCode, feedback: DjangoFeedback) -> DjangoHistoricEntry:
        return DjangoHistoricEntry(uuid.uuid4(), datetime.now(), game, code_guess, feedback)
