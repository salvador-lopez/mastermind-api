import uuid
from unittest import TestCase
from unittest.mock import Mock

from src.domain.game.entity.game import Game
from src.domain.game.entity.historicEntry import HistoricEntry
from src.domain.game.repository.gameRepository import GameRepository
from src.domain.game.repository.historicEntryRepository import HistoricEntryRepository
from src.useCase.getHistoric.getHistoricByGameIdDataTransformer import GetHistoricByGameIdDataTransformer
from src.useCase.getHistoric.getHistoricByGameIdRequest import GetHistoricByGameIdRequest
from src.useCase.getHistoric.getHistoricByGameIdResponse import GetHistoricByGameIdResponse
from src.useCase.getHistoric.getHistoricByGameIdUseCase import GetHistoricByGameIdUseCase


class TestGetHistoricByGameIdUseCase(TestCase):
    def test_get_historic_and_return_the_response_transformed_as_expected(self):
        game_repository_mock = Mock(GameRepository)
        game_mock = Mock(Game)
        game_repository_mock.configure_mock(**{'find_one_by_id.return_value': game_mock})

        historic_entry_repository_mock = Mock(HistoricEntryRepository)
        historic_mock = [Mock(HistoricEntry)]
        historic_entry_repository_mock.configure_mock(**{'find_all_by_game.return_value': historic_mock})

        data_transformer_mock = Mock(GetHistoricByGameIdDataTransformer)
        response_expected = GetHistoricByGameIdResponse(historic_mock)
        data_transformer_mock.configure_mock(**{'transform.return_value': response_expected})

        use_case = GetHistoricByGameIdUseCase(
            game_repository_mock,
            historic_entry_repository_mock,
            data_transformer_mock
        )

        game_id = uuid.uuid4()
        request = GetHistoricByGameIdRequest(game_id)

        response = use_case.execute(request)

        self.assertEqual(response, response_expected)
