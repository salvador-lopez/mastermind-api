import uuid
from unittest import TestCase
from unittest.mock import Mock

from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game
from src.domain.game.repository.codeRepository import CodeRepository
from src.domain.game.repository.gameRepository import GameRepository
from src.domain.game.service.createFeedbackByCodeGuessColorsService import CreateFeedbackByCodeGuessColorsService
from src.domain.game.service.createHistoricEntryService import CreateHistoricEntryService
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsDataTransformer import \
    CreateFeedbackByCodeGuessColorsDataTransformer
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsRequest import CreateFeedbackByCodeGuessColorsRequest
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsResponse import CreateFeedbackByCodeGuessColorsResponse
from src.useCase.createFeedback.createFeedbackByCodeGuessColorsUseCase import CreateFeedbackByCodeGuessColorsUseCase


class TestCreateFeedbackByCodeGuessColorsUseCase(TestCase):
    def test_create_feedback_and_return_the_transformed_response_as_expected(self):
        game_repository_mock = Mock(GameRepository)
        game_mock = Mock(Game)
        game_repository_mock.configure_mock(**{'find_one_by_id.return_value': game_mock})

        create_feedback_by_code_guess__colors_service_mock = Mock(CreateFeedbackByCodeGuessColorsService)
        feedback_mock = Mock(Feedback)
        create_feedback_by_code_guess__colors_service_mock.configure_mock(**{'execute.return_value': feedback_mock})

        data_transformer_mock = Mock(CreateFeedbackByCodeGuessColorsDataTransformer)
        response_expected = CreateFeedbackByCodeGuessColorsResponse(feedback_mock)
        data_transformer_mock.configure_mock(**{'transform.return_value': response_expected})

        use_case = CreateFeedbackByCodeGuessColorsUseCase(
            game_repository_mock,
            create_feedback_by_code_guess__colors_service_mock,
            Mock(CreateHistoricEntryService),
            Mock(CodeRepository),
            data_transformer_mock
        )
        code_peg_color = CodePegColor('RED')
        code_peg_colors = [code_peg_color, code_peg_color, code_peg_color, code_peg_color]
        game_id = uuid.uuid4()
        request = CreateFeedbackByCodeGuessColorsRequest(game_id, code_peg_colors)

        response = use_case.execute(request)

        self.assertEqual(response, response_expected)

    def test_create_historic_entry(self):

        game_repository_mock = Mock(GameRepository)
        game_mock = Mock(Game)
        game_repository_mock.configure_mock(**{'find_one_by_id.return_value': game_mock})

        create_feedback_by_code_guess__colors_service_mock = Mock(CreateFeedbackByCodeGuessColorsService)
        feedback_mock = Mock(Feedback)
        create_feedback_by_code_guess__colors_service_mock.configure_mock(**{'execute.return_value': feedback_mock})

        create_game_historic_entry_service_mock = Mock(CreateHistoricEntryService)

        code_repository_mock = Mock(CodeRepository)
        code_guess_mock = Mock(Code)
        code_repository_mock.configure_mock(**{'find_one_by_colors.return_value': code_guess_mock})

        data_transformer_mock = Mock(CreateFeedbackByCodeGuessColorsDataTransformer)
        response_expected = CreateFeedbackByCodeGuessColorsResponse(feedback_mock)
        data_transformer_mock.configure_mock(**{'transform.return_value': response_expected})

        use_case = CreateFeedbackByCodeGuessColorsUseCase(
            game_repository_mock,
            create_feedback_by_code_guess__colors_service_mock,
            create_game_historic_entry_service_mock,
            code_repository_mock,
            data_transformer_mock
        )
        code_peg_color = CodePegColor('RED')
        code_peg_colors = [code_peg_color, code_peg_color, code_peg_color, code_peg_color]
        game_id = uuid.uuid4()
        request = CreateFeedbackByCodeGuessColorsRequest(game_id, code_peg_colors)

        use_case.execute(request)

        create_game_historic_entry_service_mock.execute.assert_called_once_with(
            game_mock,
            code_guess_mock,
            feedback_mock
        )
