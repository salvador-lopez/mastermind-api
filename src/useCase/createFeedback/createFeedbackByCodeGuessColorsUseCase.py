from typing import Any

from src.domain.game.entity.game import Game
from src.domain.game.repository.codeRepository import CodeRepository
from src.domain.game.repository.gameRepository import GameRepository
from src.domain.game.service.createHistoricEntryService import CreateHistoricEntryService
from src.domain.game.service.createFeedbackByCodeGuessColorsService import CreateFeedbackByCodeGuessColorsService
from src.domain.game.entity.feedback import Feedback
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsDataTransformer import CreateFeedbackByCodeGuessColorsDataTransformer
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsRequest import CreateFeedbackByCodeGuessColorsRequest
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsResponse import CreateFeedbackByCodeGuessColorsResponse


class CreateFeedbackByCodeGuessColorsUseCase:

    def __init__(
            self,
            game_repository: GameRepository,
            create_feedback_by_code_guess__colors_service: CreateFeedbackByCodeGuessColorsService,
            create_game_historic_entry_service: CreateHistoricEntryService,
            code_repository: CodeRepository,
            data_transformer: CreateFeedbackByCodeGuessColorsDataTransformer
    ):
        self._game_repository = game_repository
        self._create_feedback_by_code_guess_colors_service = create_feedback_by_code_guess__colors_service
        self._create_game_historic_entry_service = create_game_historic_entry_service
        self._code_repository = code_repository
        self._data_transformer = data_transformer

    def execute(self, request: CreateFeedbackByCodeGuessColorsRequest) -> Any:
        game = self._game_repository.find_one_by_id(request.game_id)
        code_guess_colors = request.colors

        feedback = self._create_feedback_by_code_guess_colors_service.execute(game, code_guess_colors)

        self._add_entry_to_game_historic(game, code_guess_colors, feedback)

        return self._data_transformer.transform(CreateFeedbackByCodeGuessColorsResponse(feedback))

    def _add_entry_to_game_historic(self, game: Game, code_guess_colors: [CodePegColor], feedback: Feedback):
        """
        TODO Here we should dispatch a domain event (FeedbackCreatedEvent) and this Code should be executed in a
             DomainEventListener. Investigate how to implement a DomainEventDispatcher (maybe with Django signals?)
        """
        code_guess = self._code_repository.find_one_by_colors(code_guess_colors)
        self._create_game_historic_entry_service.execute(game, code_guess, feedback)
