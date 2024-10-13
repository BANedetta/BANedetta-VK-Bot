from banedetta_mfb import Polling
from main import db

async def polling():
	polling = Polling(db)
	print(1)

	async for raw in polling.polling():
		print(raw)