from src.infrastructure.presentation.dataTransformation.codeToApiResourceDictionary import CodeToApiResourceDictionary
from src.infrastructure.presentation.dataTransformation.createGame.createGameResponseToApiResourceDictionary import \
    CreateGameResponseToApiResourceDictionary

from src.infrastructure.presentation.dataTransformation.createFeedback.createFeedbackByCodeGuessColorsResponseToApiResourceDictionary import \
    CreateFeedbackByCodeGuessColorsResponseToApiResourceDictionary
from src.infrastructure.presentation.dataTransformation.feedbackToApiResourceDictionary import \
    FeedbackToApiResourceDictionary
from src.infrastructure.presentation.dataTransformation.getHistoric.getHistoricByGameIdToApiResourceDictionary import \
    GetHistoricByGameIdToApiResourceDictionary


class CreateGameResponseToApiResourceDictionaryStaticFactory:
    @staticmethod
    def create() -> CreateGameResponseToApiResourceDictionary:
        return CreateGameResponseToApiResourceDictionary()


class FeedbackToApiResourceDictionaryStaticFactory:
    @staticmethod
    def create() -> FeedbackToApiResourceDictionary:
        return FeedbackToApiResourceDictionary()


class CodeToApiResourceDictionaryStaticFactory:
    @staticmethod
    def create() -> CodeToApiResourceDictionary:
        return CodeToApiResourceDictionary()


class CreateFeedbackByCodeGuessResponseToApiResourceDictionaryStaticFactory:
    @staticmethod
    def create() -> CreateFeedbackByCodeGuessColorsResponseToApiResourceDictionary:
        return CreateFeedbackByCodeGuessColorsResponseToApiResourceDictionary(
            FeedbackToApiResourceDictionaryStaticFactory.create()
        )


class GetHistoricByGameIdToApiResourceDictionaryStaticFactory:
    @staticmethod
    def create() -> GetHistoricByGameIdToApiResourceDictionary:
        return GetHistoricByGameIdToApiResourceDictionary(
            CodeToApiResourceDictionaryStaticFactory.create(),
            FeedbackToApiResourceDictionaryStaticFactory.create()
        )
