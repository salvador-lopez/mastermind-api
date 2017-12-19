from unittest import TestCase
from unittest.mock import Mock

from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game
from src.domain.game.entity.historicEntry import HistoricEntry
from src.domain.game.factory.historicEntryFactory import HistoricEntryFactory
from src.domain.game.repository.historicEntryRepository import HistoricEntryRepository
from src.domain.game.service.createHistoricEntryService import CreateHistoricEntryService


class TestCreateHistoricEntryService(TestCase):
    def test_will_create_and_save_historic_entry_as_expected(self):
        historic_entry_factory_mock = Mock(HistoricEntryFactory)
        historic_entry_expected = Mock(HistoricEntry)
        historic_entry_factory_mock.configure_mock(**{'create.return_value': historic_entry_expected})
        historic_entry_repository_mock = Mock(HistoricEntryRepository)

        create_historic_entry_service = CreateHistoricEntryService(
            historic_entry_factory_mock,
            historic_entry_repository_mock
        )

        game_mock = Mock(Game)
        code_mock = Mock(Code)
        feedback_mock = Mock(Feedback)
        create_historic_entry_service.execute(game_mock, code_mock, feedback_mock)

        historic_entry_repository_mock.save.assert_called_once_with(historic_entry_expected)
