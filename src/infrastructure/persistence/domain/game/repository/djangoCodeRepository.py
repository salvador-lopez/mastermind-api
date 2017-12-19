from src.domain.game.repository.codeRepository import CodeRepository
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode
from src.infrastructure.persistence.domain.game.entity.djangoCodePeg import DjangoCodePeg


class DjangoCodeRepository(CodeRepository):

    def find_one_by_colors(self, colors: [CodePegColor]):

        color_values = []
        for color in colors:
            color_values.append(color.value)

        code_pegs = DjangoCodePeg.objects.filter(_color_value__in=color_values).values_list('_id', flat=True)

        return DjangoCode.objects.filter(_code_pegs__djangocodecodepeg___code_peg__in=code_pegs).first()

    def save(self, code: DjangoCode):
        DjangoCode.save(code)
