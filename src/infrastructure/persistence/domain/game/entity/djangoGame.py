from django.db import models
from django.utils import timezone

from src.domain.game.entity.game import Game
from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode


class DjangoGame(Game, models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'games'

    _id = models.UUIDField(primary_key=True, editable=False, unique=True, db_column='id')
    _created_at = models.DateTimeField(editable=False, db_column='created_at', default=timezone.now)
    _code = models.ForeignKey(DjangoCode, db_column='code_id', on_delete=models.CASCADE)

    def __init__(self, id, created_at, code):
        models.Model.__init__(self)

        if not isinstance(code, DjangoCode):
            code = DjangoCode.objects.get(pk=code)

        Game.__init__(self, id, created_at, code)
