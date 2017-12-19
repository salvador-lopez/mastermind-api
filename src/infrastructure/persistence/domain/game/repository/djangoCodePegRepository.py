from src.domain.game.repository.codePegRepository import CodePegRepository
from src.domain.game.valueObject.codePegColor import CodePegColor
from src.infrastructure.persistence.domain.game.entity.djangoCodePeg import DjangoCodePeg


class DjangoCodePegRepository(CodePegRepository):

    def find_one_by_color(self, color: CodePegColor) -> DjangoCodePeg:
        return DjangoCodePeg.objects.get(_color_value=color.value)
