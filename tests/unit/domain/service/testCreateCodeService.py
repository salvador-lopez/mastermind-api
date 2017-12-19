from unittest import TestCase
from unittest.mock import Mock

from src.domain.game.entity.code import Code
from src.domain.game.entity.codePeg import CodePeg
from src.domain.game.factory.codeFactory import CodeFactory
from src.domain.game.repository.codeRepository import CodeRepository
from src.domain.game.service.createCodeService import CreateCodeService


class TestCreateCodeService(TestCase):
    def test_will_create_and_save_and_return_code_as_expected(self):
        code_factory_mock = Mock(CodeFactory)
        code_expected = Mock(Code)
        code_factory_mock.configure_mock(**{'create.return_value': code_expected})
        code_repository_mock = Mock(CodeRepository)

        create_code_service = CreateCodeService(code_factory_mock, code_repository_mock)
        code_pegs = [Mock(CodePeg)]
        code = create_code_service.execute(code_pegs)

        code_repository_mock.save.assert_called_once_with(code_expected)
        self.assertIs(code_expected, code)
