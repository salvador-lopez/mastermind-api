from abc import ABC, abstractmethod

from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg


class CodeFactory(ABC):
    @abstractmethod
    def create(self, code_pegs: [CodePeg]) -> Code:
        pass
