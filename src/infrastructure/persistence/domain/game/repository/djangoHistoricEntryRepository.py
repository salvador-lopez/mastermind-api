from src.domain.game.repository.historicEntryRepository import HistoricEntryRepository
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame
from src.infrastructure.persistence.domain.game.entity.djangoHistoricEntry import DjangoHistoricEntry


class DjangoHistoricEntryRepository(HistoricEntryRepository):

    def save(self, historic_entry: DjangoHistoricEntry):
        DjangoHistoricEntry.save(historic_entry)

    def find_all_by_game(self, game: DjangoGame) -> [DjangoHistoricEntry]:
        return list(DjangoHistoricEntry.objects.filter(_game=game))
