from aiovk import TokenSession
from asyncio import get_event_loop, gather
from banedetta_mfb import DB
from config import config
from dotenv import load_dotenv
from os import getenv

load_dotenv(override = True)

db = DB(
	getenv("host"), getenv("user"), getenv("password"),
	getenv("schema"), int(getenv("port"))
)

vk = TokenSession(getenv("token"))
vk.API_VERSION = "5.199"

async def init_db():
	await db.init()
	from bot.listeners.db_listener import polling
	await polling()

async def init_longpoll():
	from bot.listeners.vk_longpoll import longpolling
	await longpolling()

async def main():
	await gather(init_longpoll(), init_db())

if __name__ == "__main__":
	loop = get_event_loop()
	loop.run_until_complete(main())
