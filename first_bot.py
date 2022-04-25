
from aiogram.utils import executor
from create_bot import dp
from handler import client, admin, common


async def on_startup(_):
    print('bot online')


client.register_handlers_client(dp)
common.register_handlers_common(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
