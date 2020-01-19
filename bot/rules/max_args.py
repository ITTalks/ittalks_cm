from vk.bot_framework.dispatcher.rule import NamedRule
import typing
from vk import types


class ArgsRange(NamedRule):
    key = "args_range"

    def __init__(self, args_range: typing.Tuple[int, int]):
        self.args_range = args_range

    async def check(self, message: types.Message, data: dict):
        text = message.text.split()[1:]
        _accepted = False
        if self.args_range[0] <= len(text) <= self.args_range[1]:
            _accepted = True
        return _accepted
