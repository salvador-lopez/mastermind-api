from abc import ABC, abstractmethod
from typing import Any

from src.useCase.createFeedback.createFeedbackByCodeGuessColorsResponse import CreateFeedbackByCodeGuessColorsResponse


class CreateFeedbackByCodeGuessColorsDataTransformer(ABC):
    @abstractmethod
    def transform(self, response: CreateFeedbackByCodeGuessColorsResponse) -> Any:
        pass
