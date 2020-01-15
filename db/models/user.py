import time
import typing

import umongo
from umongo import fields

from ..db import Instance


instance: umongo.Instance = Instance.get_current().instance


@instance.register
class User(umongo.Document):
    uid = fields.IntegerField(required=True, unique=True)
    created_time = fields.IntegerField(default=time.time)

    class Meta:
        collection = instance.db.users

    @staticmethod
    async def create_user(uid: int) -> typing.Union["User", typing.NoReturn]:
        user: User = User(uid=uid)
        await user.commit()
        return user

    @staticmethod
    async def get_user(uid: int) -> typing.Union["User", typing.NoReturn]:
        user = await User.find_one({"uid": uid})
        return user
