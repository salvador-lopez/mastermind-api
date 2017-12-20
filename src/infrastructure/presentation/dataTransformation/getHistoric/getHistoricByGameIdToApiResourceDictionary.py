from src.domain.game.entity.historicEntry import HistoricEntry
from src.infrastructure.presentation.dataTransformation.codeToApiResourceDictionary import CodeToApiResourceDictionary
from src.infrastructure.presentation.dataTransformation.feedbackToApiResourceDictionary import \
    FeedbackToApiResourceDictionary
from src.useCase.getHistoric.getHistoricByGameIdDataTransformer import GetHistoricByGameIdDataTransformer
from src.useCase.getHistoric.getHistoricByGameIdResponse import GetHistoricByGameIdResponse


class GetHistoricByGameIdToApiResourceDictionary(GetHistoricByGameIdDataTransformer):

    def __init__(
            self,
            code_to_api_resource_dictionary: CodeToApiResourceDictionary,
            feedback_to_api_resource_dictionary: FeedbackToApiResourceDictionary
    ):
        self._code_to_api_resource_dictionary = code_to_api_resource_dictionary
        self._feedback_to_api_resource_dictionary = feedback_to_api_resource_dictionary

    def transform(self, response: GetHistoricByGameIdResponse) -> dict:
        historic = response.historic

        historic_entries = []

        for historic_entry in historic:
            historic_entries.append(self._build_historic_entry_dict(historic_entry))

        return {'historic': historic_entries}

    def _build_historic_entry_dict(self, historic_entry: HistoricEntry) -> dict:
        return {
            "id": historic_entry.id,
            "game_id": historic_entry.game.id,
            "code_guess": self._code_to_api_resource_dictionary.transform(historic_entry.code_guess),
            "feedback": self._feedback_to_api_resource_dictionary.transform(historic_entry.game_feedback)
        }
