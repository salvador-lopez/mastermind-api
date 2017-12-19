from abc import ABC, abstractmethod
from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.valueObject.codePegColor import CodePegColor


class CodePegRepository(ABC):

    @abstractmethod
    def find_one_by_color(self, color: CodePegColor) -> CodePeg:
        pass
