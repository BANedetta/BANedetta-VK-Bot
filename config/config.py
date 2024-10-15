# VK Group id (without a minus sign)
group_id = 224130500

# Post templates
post_templates = {
	"waiting": {
		"attachments": "photo-224130500_457239036",
		"post": """
Игрок {banned} был заблокирован игроком {by}.
Причина: {reason}.
Ожидается доказательства в течение 6 часов, в ином случае ваш аккаунт будет заблокирован!
		"""
	},
	"confirmed": {
		"attachments": "photo-224130500_457239042",
		"post": """
Игрок {banned} был заблокирован игроком {by}.
Причина: {reason}.
Подтверждено!
		"""
	},
	"denied": {
		"attachments": "photo-224130500_457239037",
		"post": """
Игрок {banned} был заблокирован игроком {by}.
Причина: {reason}.
Не подтверждено! {banned} был разблокирован, а {by} заблокирован.
		"""
	},
}