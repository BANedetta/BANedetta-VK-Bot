from aiovk import TokenSession
from aiovk.longpoll import BotsLongPoll
from dotenv import load_dotenv
from main import vk
from os import getenv

load_dotenv()

async def longpolling():
	longpoll = BotsLongPoll(vk, getenv("group_id"))
	print(2)

	async for event in longpoll.iter():
		print(event)
