from abc import ABC, abstractmethod

from src.domain.game.entity.game import Game
from src.domain.game.entity.historicEntry import HistoricEntry


class HistoricEntryRepository(ABC):
    @abstractmethod
    def save(self, historic_entry: HistoricEntry):
        pass

    @abstractmethod
    def find_all_by_game(self, game: Game) -> [HistoricEntry]:
        pass
