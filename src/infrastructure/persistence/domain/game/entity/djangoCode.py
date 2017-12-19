from django.db import models
from django.utils import timezone

from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg
from src.infrastructure.persistence.domain.game.entity.djangoCodeCodePeg import DjangoCodeCodePeg
from src.infrastructure.persistence.domain.game.entity.djangoCodePeg import DjangoCodePeg


class DjangoCode(Code, models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'game_codes'

    _id = models.UUIDField(primary_key=True, editable=False, unique=True, db_column='id')
    _created_at = models.DateTimeField(editable=False, db_column='created_at', default=timezone.now)
    _code_pegs = models.ManyToManyField(DjangoCodePeg, db_column='code_pegs', through=DjangoCodeCodePeg, symmetrical=False)

    def __init__(self, id, created_at, code_pegs=None):
        models.Model.__init__(self)
        Code.__init__(self, id, created_at, code_pegs)

    def set_code_pegs(self, code_pegs):
        if code_pegs is not None:
            self.save()
            for code_peg in code_pegs:
                DjangoCodeCodePeg.save(DjangoCodeCodePeg(_code_id=self.id, _code_peg_id=code_peg.id))

    @property
    def code_pegs(self) -> [CodePeg]:
        return self._code_pegs.all()
