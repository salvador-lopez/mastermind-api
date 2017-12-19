from django.db import models
from django.utils import timezone

from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.valueObject.codePegColor import CodePegColor


class DjangoCodePeg(CodePeg, models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'game_code_pegs'

    _id = models.UUIDField(primary_key=True, editable=False, unique=True, db_column='id')
    _created_at = models.DateTimeField(editable=False, db_column='created_at', default=timezone.now)
    _color_value = models.TextField(db_column='color')

    @property
    def color(self):
        return CodePegColor(self._color_value)
