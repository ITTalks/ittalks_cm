import logging
import typing
from vk.bot_framework import BaseMiddleware
from vk.types.events.community.event import BaseEvent, MessageNew
from vk import VK

from db.models.user import User

logger = logging.getLogger(__name__)


class UsersRegistrationMiddleware(BaseMiddleware):
    async def pre_process_event(
        self, event: typing.Type[BaseEvent], data: dict
    ) -> dict:
        if event.type != "message_new":
            return data

        event: MessageNew

        usr: User = await User.get_user(event.object.message.from_id)
        if usr:
            data["current_user"] = usr
            return data

        vk = VK.get_current()
        uid = event.object.message.from_id
        name = await vk.api_request("users.get", params={"user_ids": uid})
        first_name = name[0]["first_name"]
        second_name = name[0]["last_name"]
        usr = await User.create_user(uid=uid, nickname=f"{first_name} {second_name}")
        logger.info(
            f"User with id ({event.object.message.from_id}) succesfully registered!"
        )
        data["current_user"] = usr
        return data


__all__ = ["UsersRegistrationMiddleware"]
