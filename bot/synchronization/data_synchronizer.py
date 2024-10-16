from ..managers import posts_manager
from banedetta_db import DataSynchronizer
from main import db

async def synchronization():
	ds = DataSynchronizer(db, "vk")

	async for data in ds.synchronize_problems():
		match data["problem"]:
			case "no_post":
				post_id = await posts_manager.create_post(data)
				await db.update_post_id("vk", post_id, data["id"])

			case "resolved":
				await posts_manager.edit_post(data)
				await db.update_post_id("vk", -1, data["id"])
