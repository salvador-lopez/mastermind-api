from abc import ABC, abstractmethod

from src.domain.game.entity.game import Code
from src.domain.game.valueObject.codePegColor import CodePegColor


class CodeRepository(ABC):
    @abstractmethod
    def find_one_by_colors(self, colors: [CodePegColor]):
        pass

    @abstractmethod
    def save(self, code: Code):
        pass
