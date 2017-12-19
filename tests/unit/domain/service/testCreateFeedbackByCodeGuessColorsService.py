import uuid
from unittest import TestCase
from unittest.mock import Mock

from datetime import datetime

from src.domain.game.entity.code import Code
from src.domain.game.entity.feedback import Feedback
from src.domain.game.entity.game import Game
from src.domain.game.factory.feedbackFactory import FeedbackFactory
from src.domain.game.repository.feedbackRepository import FeedbackRepository
from src.domain.game.service.createFeedbackByCodeGuessColorsService import CreateFeedbackByCodeGuessColorsService
from src.domain.game.valueObject.codePegColor import CodePegColor
from tests.unit.domain.entity.testableCodePeg import TestableCodePeg


class TestCreateFeedbackByCodeGuessColorsService(TestCase):
    def test_it_should_create_feedback_and_save_and_return_it_as_expected(self):
        feedback_factory_mock = Mock(FeedbackFactory)
        feedback_expected = Mock(Feedback)
        feedback_factory_mock.configure_mock(**{'create.return_value': feedback_expected})
        feedback_repository_mock = Mock(FeedbackRepository)

        create_feedback_service = CreateFeedbackByCodeGuessColorsService(
            feedback_factory_mock,
            feedback_repository_mock
        )
        code_guess_colors = [CodePegColor('RED'), CodePegColor('GREEN'), CodePegColor('RED'), CodePegColor('YELLOW')]

        red_code_peg = TestableCodePeg(uuid.uuid4(), CodePegColor('RED'))
        blue_code_peg = TestableCodePeg(uuid.uuid4(), CodePegColor('RED'))
        green_code_peg = TestableCodePeg(uuid.uuid4(), CodePegColor('GREEN'))

        code_pegs = [red_code_peg, blue_code_peg, green_code_peg, red_code_peg]
        code = Code(uuid.uuid4(), datetime.now(), code_pegs)

        game = Game(uuid.uuid4(), datetime.now(), code)

        feedback = create_feedback_service.execute(game, code_guess_colors)

        feedback_repository_mock.save.assert_called_once_with(feedback_expected)
        self.assertIs(feedback_expected, feedback)

        black_pegs_expected = 1
        white_pegs_expected = 2

        feedback_factory_mock.create.assert_called_once_with(black_pegs_expected, white_pegs_expected)
