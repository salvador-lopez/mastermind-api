from abc import ABC, abstractmethod
from typing import Any

from src.useCase.getHistoric.getHistoricByGameIdResponse import GetHistoricByGameIdResponse


class GetHistoricByGameIdDataTransformer(ABC):
    @abstractmethod
    def transform(self, response: GetHistoricByGameIdResponse) -> Any:
        pass
