from src.domain.game.entity.feedback import Feedback


class FeedbackToApiResourceDictionary:
    def transform(self, feedback: Feedback) -> dict:
        return {'id': feedback.id, 'feedback': self.get_feedback_string(feedback)}

    def get_feedback_string(self, feedback: Feedback) -> str:
        black_pegs = feedback.black_pegs
        white_pegs = feedback.white_pegs

        return str(black_pegs) + ' ' + self._pluralize_if_needed(black_pegs, 'black', 'blacks') + ', ' + str(
            white_pegs) + ' ' + self._pluralize_if_needed(white_pegs, 'white', 'whites')

    def _pluralize_if_needed(self, number_of_elements: int, singular_word: str, plural_word: str) -> str:
        if number_of_elements == 1:
            return singular_word
        return plural_word
