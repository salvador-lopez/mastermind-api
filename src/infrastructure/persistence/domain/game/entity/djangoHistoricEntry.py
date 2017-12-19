import uuid

from datetime import datetime

from src.domain.game.entity.historicEntry import HistoricEntry
from django.db import models
from django.utils import timezone

from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode
from src.infrastructure.persistence.domain.game.entity.djangoFeedback import DjangoFeedback
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame


class DjangoHistoricEntry(HistoricEntry, models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'game_historic_entries'

    _id = models.UUIDField(primary_key=True, unique=True, db_column='id')
    _created_at = models.DateTimeField(editable=False, db_column='created_at', default=timezone.now)
    _game = models.ForeignKey(DjangoGame, on_delete=models.DO_NOTHING, db_column='game_id')
    _code_guess = models.ForeignKey(DjangoCode, on_delete=models.DO_NOTHING, db_column='code_guess_id')
    _feedback = models.ForeignKey(DjangoFeedback, on_delete=models.DO_NOTHING, db_column='feedback_id')

    def __init__(self, id: uuid, created_at: datetime, game: DjangoGame, code_guess: DjangoCode, feedback: DjangoFeedback):
        models.Model.__init__(self)

        if isinstance(feedback, DjangoFeedback):
            self._feedback_id = feedback.id

        if not isinstance(game, DjangoGame):
            game = DjangoGame.objects.get(pk=game)

        if not isinstance(code_guess, DjangoCode):
            code_guess = DjangoCode.objects.get(pk=code_guess)

        if not isinstance(feedback, DjangoFeedback):
            feedback = DjangoFeedback.objects.get(pk=feedback)

        HistoricEntry.__init__(self, id, created_at, game, code_guess, feedback)
