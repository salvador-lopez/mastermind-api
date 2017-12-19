from typing import Any

from src.domain.game.repository.gameRepository import GameRepository
from src.domain.game.repository.historicEntryRepository import HistoricEntryRepository
from src.useCase.getHistoric.getHistoricByGameIdDataTransformer import GetHistoricByGameIdDataTransformer
from src.useCase.getHistoric.getHistoricByGameIdRequest import GetHistoricByGameIdRequest
from src.useCase.getHistoric.getHistoricByGameIdResponse import GetHistoricByGameIdResponse


class GetHistoricByGameIdUseCase:

    def __init__(
            self,
            game_repository: GameRepository,
            historic_entry_repository: HistoricEntryRepository,
            data_transformer: GetHistoricByGameIdDataTransformer
    ):
        self._game_repository = game_repository
        self._historic_entry_repository = historic_entry_repository
        self._data_transformer = data_transformer

    def execute(self, request: GetHistoricByGameIdRequest) -> Any:
        game = self._game_repository.find_one_by_id(request.game_id)

        historic = self._historic_entry_repository.find_all_by_game(game)

        return self._data_transformer.transform(GetHistoricByGameIdResponse(historic))
