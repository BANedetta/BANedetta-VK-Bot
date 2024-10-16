from ..managers import posts_manager
from aiovk.longpoll import BotsLongPoll
from main import vk, config, db

async def longpolling():
	longpoll = BotsLongPoll(vk, config.group_id)

	async for event in longpoll.iter():
		statuses = {
			"+": "confirmed",
			"-": "denied"
		}
		object = event["object"]

		if (
			event["type"] != "wall_reply_new" or
			not object["from_id"] in config.users
		):
			continue

		if data := await db.get_data_by_post_id("vk", object["post_id"]):
			if (status := data["status"]) == "waiting":
				match status := statuses.get(object["text"]):
					case "confirmed": await db.confirm(data["id"])
					case "denied": await db.deny(data["id"])
					case _: continue

			data["status"] = status
			await posts_manager.edit_post(data)
			await db.update_post_id("vk", -1, data["id"])
