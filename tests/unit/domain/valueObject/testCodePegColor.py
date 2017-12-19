from unittest import TestCase

from src.domain.game.valueObject.codePegColor import CodePegColor


class TestCodePegColor(TestCase):
    def test_raise_value_error_when_color_is_not_allowed(self):
        with self.assertRaises(ValueError):
            CodePegColor('BLACK')

    def test_can_be_created_with_allowed_value(self):
        color = CodePegColor('GREEN')
        self.assertIs('GREEN', color.value)
