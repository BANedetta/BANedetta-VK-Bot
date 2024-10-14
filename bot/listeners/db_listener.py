from ..managers import posts_manager
from banedetta_mfb import Polling
from main import db

async def polling():
	polling = Polling(db)

	async for raw in polling.polling():
		if raw["confirmed"]: continue

		post_id = (await posts_manager.create_post(raw))
		await db.update_post_id("vk", post_id, raw["id"])
