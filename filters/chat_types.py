from aiogram import types
from aiogram.filters import Filter


class ChatTypeFilter(Filter):
    def __init__(self, chat_type: list[str]) -> None:
        self.chat_type = chat_type

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_type
