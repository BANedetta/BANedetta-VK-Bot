from ..managers import posts_manager
from aiovk.longpoll import BotsLongPoll
from main import vk, config, db

async def longpolling():
	longpoll = BotsLongPoll(vk, config.group_id)
	statuses = {"+": "confirmed", "-": "denied"}

	async for event in longpoll.iter():
		if event["type"] != "wall_reply_new" or event["object"]["from_id"] not in config.users:
			continue

		if data := await db.get_data_by_post_id("vk", event["object"]["post_id"]):
			if data["status"] == "waiting" and (status := statuses.get(event["object"]["text"])):
				await (db.confirm if status == "confirmed" else db.deny)(data["id"])
				data["status"] = status
				await posts_manager.edit_post(data)
				await db.update_post_id("vk", -1, data["id"])
