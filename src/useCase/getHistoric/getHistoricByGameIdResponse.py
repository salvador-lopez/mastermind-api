from src.domain.game.entity.historicEntry import HistoricEntry


class GetHistoricByGameIdResponse:

    def __init__(self, historic: [HistoricEntry]):
        self._historic = historic

    @property
    def historic(self) -> [HistoricEntry]:
        return self._historic
