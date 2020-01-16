from vk.bot_framework import BaseRule
from vk import types
from config import admins


class IsAdmin(BaseRule):
    def __init__(self, is_admin: bool):
        self.is_admin: bool = is_admin

    async def check(self, message: types.Message, data: dict):
        return message.from_id in admins
