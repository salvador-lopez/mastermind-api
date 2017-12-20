from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg


class CodeToApiResourceDictionary:
    def transform(self, code: Code) -> dict:
        return {'id': code.id, 'code_pegs': self._build_code_pegs_string(code.code_pegs)}

    def _build_code_pegs_string(self, code_pegs: [CodePeg]) -> str:
        code_pegs_list = []

        for code_peg in code_pegs:
            code_pegs_list.append(code_peg.color.value)

        return ", ".join(code_pegs_list)


