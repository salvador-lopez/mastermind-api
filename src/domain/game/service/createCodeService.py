from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.factory.codeFactory import CodeFactory
from src.domain.game.repository.codeRepository import CodeRepository


class CreateCodeService:
    def __init__(self, code_factory: CodeFactory, code_repository: CodeRepository):
        self._code_factory = code_factory
        self._code_repository = code_repository

    def execute(self, code_pegs: [CodePeg]) -> Code:
        code = self._code_factory.create(code_pegs)

        self._code_repository.save(code)

        return code
