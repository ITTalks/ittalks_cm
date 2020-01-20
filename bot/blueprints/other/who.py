from vk import types
from vk.bot_framework.dispatcher import Blueprint
import vk
from vk.bot_framework import get_group_id
import random

bp = Blueprint()


@bp.message_handler(commands=["кто"], in_chat=True)
async def who_is(message: types.Message, _):
    vk_ = vk.VK.get_current()
    q = message.text.split()[1:]
    params = {"peer_id": message.peer_id, "group_id": await get_group_id(vk_)}
    users = await vk_.api_request("messages.getConversationMembers", params=params)
    random_user = random.choice(users["profiles"])
    await message.answer(
        f"Скорее всего {' '.join(q)} - "
        f"{random_user['first_name']}"
        f" {random_user['last_name']}"
    )
