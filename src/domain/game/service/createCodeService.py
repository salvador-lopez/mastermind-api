from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.factory.codeFactory import CodeFactory
from src.domain.game.repository.codeRepository import CodeRepository


class CreateCodeService(CodeFactory, CodeRepository):

    def execute(self, code_pegs: [CodePeg]) -> Code:
        code = super().create(code_pegs)

        super().save(code)

        return code
