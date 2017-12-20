from src.infrastructure.presentation.dataTransformation.createGame.djangoHttpRequestToCreateGameRequest import \
    DjangoHttpRequestToCreateGameRequest
from src.infrastructure.presentation.dataTransformation.createFeedback.djangoHttpRequestToCreateFeedbackByCodeGuessColorsRequest import \
    DjangoHttpRequestToCreateFeedbackByCodeGuessRequest


class DjangoHttpRequestToCreateGameRequestStaticFactory:
    @staticmethod
    def create() -> DjangoHttpRequestToCreateGameRequest:
        return DjangoHttpRequestToCreateGameRequest()


class DjangoHttpRequestToCreateFeedbackByCodeGuessRequestStaticFactory:
    @staticmethod
    def create() -> DjangoHttpRequestToCreateFeedbackByCodeGuessRequest:
        return DjangoHttpRequestToCreateFeedbackByCodeGuessRequest()
