from vk.utils import TaskManager
from vk import VK
from vk.bot_framework import Dispatcher
from vk.bot_framework import get_group_id
import logging
import os
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(level=logging.DEBUG)
vk = VK(access_token=os.getenv("TOKEN"))
dp = Dispatcher(vk)


async def run():
    group_id = await get_group_id(vk)
    dp.run_polling(group_id)


if __name__ == "__main__":
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
