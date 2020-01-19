from vk import types
from vk.bot_framework.dispatcher import Blueprint
from bot.rules.admin import IsAdmin

bp = Blueprint()


@bp.message_handler(IsAdmin(True), commands=["call"], in_chat=True)
async def call_command(message: types.Message, _):
    await message.answer(f"debug: {message}")
