from django.db import models

from src.infrastructure.persistence.domain.game.entity.djangoCodePeg import DjangoCodePeg


class DjangoCodeCodePeg(models.Model):
    class Meta:
        app_label = 'games'
        db_table = 'game_codes__code_pegs'

    _id = models.AutoField(primary_key=True, db_column='id')
    _code = models.ForeignKey('DjangoCode', on_delete=models.CASCADE, db_column='djangocode_id')
    _code_peg = models.ForeignKey(DjangoCodePeg, on_delete=models.CASCADE, db_column='djangocodepeg_id')

