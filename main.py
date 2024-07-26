import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.strategy import FSMStrategy

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import router as user_private_router
from utils.comands import private


ALLOWED_UPDATES = ["message"]

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    print("start bot")
    asyncio.run(main())
