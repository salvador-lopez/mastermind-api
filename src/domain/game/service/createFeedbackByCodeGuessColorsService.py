from src.domain.game.entity.game import Game
from src.domain.game.factory.feedbackFactory import FeedbackFactory
from src.domain.game.repository.feedbackRepository import FeedbackRepository
from src.domain.game.entity.feedback import Feedback
from src.domain.game.valueObject.codePegColor import CodePegColor


class CreateFeedbackByCodeGuessColorsService:
    def __init__(self, feedback_factory: FeedbackFactory, feedback_repository: FeedbackRepository):
        self._feedback_factory = feedback_factory
        self._feedback_repository = feedback_repository

    def execute(self, game: Game, code_guess_colors: [CodePegColor]) -> Feedback:
        black_pegs = 0
        white_pegs = 0

        for color_position, color in enumerate(code_guess_colors):
            game_code = game.code
            code_pegs = game_code.code_pegs
            for code_peg_position, code_peg in enumerate(code_pegs):
                if color.equal(code_peg.color):
                    if color_position == code_peg_position:
                        black_pegs += 1
                    else:
                        white_pegs += 1
                    break

        feedback = self._feedback_factory.create(black_pegs, white_pegs)

        self._feedback_repository.save(feedback)

        return feedback
