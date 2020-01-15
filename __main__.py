from vk.utils import TaskManager
from vk import VK
from vk.bot_framework import Dispatcher
from vk.bot_framework import get_group_id
import logging
import os
from dotenv import load_dotenv
from bot.middlewares import UsersRegistrationMiddleware
from bot.blueprints import (
    karma_bp,
    message_bp,
    add_karma_bp,
    karma_top_bp,
    nick_bp,
    info_bp,
)


load_dotenv()
logging.basicConfig(level=logging.DEBUG)
vk = VK(access_token=os.getenv("TOKEN"))
dp = Dispatcher(vk)


async def run():
    dp.setup_middleware(UsersRegistrationMiddleware())
    dp.setup_blueprint(karma_top_bp)
    dp.setup_blueprint(add_karma_bp)
    dp.setup_blueprint(karma_bp)
    dp.setup_blueprint(nick_bp)
    dp.setup_blueprint(info_bp)
    dp.setup_blueprint(message_bp)  # Этот всегда регать последним
    group_id = await get_group_id(vk)
    dp.run_polling(group_id)


if __name__ == "__main__":
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
