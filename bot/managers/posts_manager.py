from main import vk, config

async def _get_params(data: dict, post_config: dict) -> dict:
	return {
		"from_group": 1,
		"owner_id": -config.group_id,
		"attachments": post_config["attachments"],
		"message": post_config["post"].format(banned = data["banned"], by = data["by"], reason = data["reason"])
	}

async def create_post(data: dict) -> int:
	params = await _get_params(data, config.post_templates["waiting"])
	response = await vk.send_api_request("wall.post", params)
	return response["post_id"]

async def edit_post(data: dict):
	params = await _get_params(data, config.post_templates[data["status"]]) | {"post_id": data["vk_post"]}
	await vk.send_api_request("wall.edit", params)