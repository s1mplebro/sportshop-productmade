from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message
from buttons import simple_queries_templates


class IsSimpleQueryFilter(BoundFilter):
    key = "is_simple_query"

    def __init__(self):
        self.simple_queries = simple_queries_templates.keys()

    async def check(self, msg: Message):
        return True if msg.text in simple_queries_templates else False


def bind_all_custom_filters(dp):
    dp.filters_factory.bind(IsSimpleQueryFilter)