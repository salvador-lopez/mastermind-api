class CodePegColor:
    ALLOWED_VALUES = {'RED', 'GREEN', 'ORANGE', 'BLUE', 'YELLOW', 'PURPLE'}

    def __init__(self, value):
        self.set_value(value)

    def set_value(self, value: str):
        if value not in CodePegColor.ALLOWED_VALUES:
            raise ValueError('Color not allowed: ' + value)

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def equal(self, code_peg_color) -> bool:
        return self._value == code_peg_color.value
