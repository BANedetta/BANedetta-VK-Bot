from main import db
from ..managers import posts_manager
from banedetta_db import DataSynchronizer

async def synchronization():
	ds = DataSynchronizer(db, "vk")

	async for data in ds.synchronization():
		if data["status"] == "waiting" and data["vk_post"] is None:
			post_id = await posts_manager.create_post(data)
			await db.update_post_id("vk", post_id, data["id"])

		if data["status"] != "waiting" and data["vk_post"] > -1:
			await posts_manager.edit_post(data)
			await db.update_post_id("vk", -1, data["id"])