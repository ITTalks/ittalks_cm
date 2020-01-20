import logging
import os

from vk.utils import TaskManager
from vk import VK
from vk.bot_framework import Dispatcher
from vk.bot_framework import get_group_id
from dotenv import load_dotenv
from bot.middlewares import UsersRegistrationMiddleware
from bot.named_rules import ArgsRange
from bot.blueprints import (
    karma_bp,
    message_bp,
    add_karma_bp,
    karma_top_bp,
    nick_bp,
    info_bp,
    call_bp,
    who_bp,
    info_humor_bp,
    ball_bp
)


load_dotenv()
logging.basicConfig(level=logging.DEBUG)
vk = VK(access_token=os.getenv("TOKEN"))
dp = Dispatcher(vk)


async def run():
    dp.setup_middleware(UsersRegistrationMiddleware())
    dp.setup_rule(ArgsRange)
    dp.setup_blueprint(nick_bp)
    dp.setup_blueprint(karma_top_bp)
    dp.setup_blueprint(karma_bp)
    dp.setup_blueprint(info_bp)
    dp.setup_blueprint(add_karma_bp)
    dp.setup_blueprint(call_bp)
    dp.setup_blueprint(who_bp)
    dp.setup_blueprint(info_humor_bp)
    dp.setup_blueprint(ball_bp)

    # Всегда должен быть последним.
    dp.setup_blueprint(message_bp)  # порядок рега блупринтов не менять!!1
    dp.run_polling(await get_group_id(vk))


if __name__ == "__main__":
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
