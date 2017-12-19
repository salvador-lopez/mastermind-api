from src.domain.game.entity.game import Game
from src.domain.game.factory.historicEntryFactory import HistoricEntryFactory
from src.domain.game.repository.historicEntryRepository import HistoricEntryRepository
from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback


class CreateHistoricEntryService:
    def __init__(self, historic_entry_factory: HistoricEntryFactory,
                 historic_entry_repository: HistoricEntryRepository):
        self._historic_entry_factory = historic_entry_factory
        self._historic_entry_repository = historic_entry_repository

    def execute(self, game: Game, code_guess: Code, feedback: Feedback):
        historic_entry = self._historic_entry_factory.create(game, code_guess, feedback)

        self._historic_entry_repository.save(historic_entry)
