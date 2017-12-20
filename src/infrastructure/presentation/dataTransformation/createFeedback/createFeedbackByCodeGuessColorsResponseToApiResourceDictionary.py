from src.infrastructure.presentation.dataTransformation.feedbackToApiResourceDictionary import \
    FeedbackToApiResourceDictionary
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsDataTransformer import CreateFeedbackByCodeGuessColorsDataTransformer
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsResponse import CreateFeedbackByCodeGuessColorsResponse


class CreateFeedbackByCodeGuessColorsResponseToApiResourceDictionary(CreateFeedbackByCodeGuessColorsDataTransformer):
    def __init__(self, feedback_to_api_resource_dictionary: FeedbackToApiResourceDictionary):
        self._feedback_to_api_resource_dictionary = feedback_to_api_resource_dictionary

    def transform(self, response: CreateFeedbackByCodeGuessColorsResponse) -> dict:
        return self._feedback_to_api_resource_dictionary.transform(response.feedback)


