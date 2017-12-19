from abc import ABC, abstractmethod
from typing import Any

from src.useCase.createGame.createGameResponse import CreateGameResponse


class CreateGameDataTransformer(ABC):
    @abstractmethod
    def transform(self, create_game_response: CreateGameResponse) -> Any:
        pass
