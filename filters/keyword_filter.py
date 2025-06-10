from aiogram.filters import BaseFilter
from aiogram.types import Message

class KeywordFilter(BaseFilter):
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    async def __call__(self, message: Message) -> bool:
        return self.keyword in message.text.lower()
