import uuid
from datetime import datetime
from django.db import models
from django.utils import timezone

from src.domain.game.entity.feedback import Feedback


class DjangoFeedback(Feedback, models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'game_feedbacks'

    _id = models.UUIDField(primary_key=True, editable=False, unique=True, db_column='id')
    _created_at = models.DateTimeField(editable=False, db_column='created_at', default=timezone.now)
    _black_pegs = models.IntegerField(db_column='black_pegs')
    _white_pegs = models.IntegerField(db_column='white_pegs')
    
    def __init__(self, id: uuid, created_at: datetime, black_pegs, white_pegs):
        models.Model.__init__(self)
        Feedback.__init__(self, id, created_at, black_pegs, white_pegs)
