import uuid

from datetime import datetime

from src.domain.game.factory.codeFactory import CodeFactory
from src.domain.game.entity.codePeg import CodePeg
from src.infrastructure.persistence.domain.game.entity.djangoCode import DjangoCode


class DjangoCodeFactory(CodeFactory):
    def create(self, code_pegs: [CodePeg]) -> DjangoCode:
        return DjangoCode(uuid.uuid4(), datetime.now(), code_pegs)
