from ..managers import posts_manager
from aiovk.longpoll import BotsLongPoll
from main import vk, config, db

async def longpolling():
	longpoll = BotsLongPoll(vk, config.group_id)

	async for event in longpoll.iter():
		object = event["object"]
		statuses = {
			"+": "confirmed",
			"-": "denied"
		}

		if (
			event["type"] != "wall_reply_new" or
			not (status := statuses.get(object["text"]))
		):
			continue

		if not (data := await db.get_data_by_post_id("vk", object["post_id"])):
			continue

		match status:
			case "confirmed": await db.confirm(data["id"])
			case "denied": await db.deny(data["id"])
			case _: raise Exception("Unknown error")

		await posts_manager.edit_post(status, data)