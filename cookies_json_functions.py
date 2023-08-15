import json


class LoadJson():
	def __init__(self, json_file_name: str) -> None:
		"""Инициализируем и работаем .json file"""
		self.json_file_name = json_file_name

	def load_json(self) -> list[dict]:
		"""Функция для открытия и загрузки .json файла"""
		with open(self.json_file_name, "r") as json_obj:
			json_data = json.load(json_obj)
		return json_data


class ChangeSameSiteInCookie():
	def __init__(self, cookies_list: list[dict]):
		"""Инициализируем cookie и работаем с ними"""
		self.cookies_list = cookies_list

	def change_same_site_value(self) -> list[dict]:
		"""Функция для изменения значения SameSite на допустимое значение в playwright(Strict)"""
		for i in range(len(self.cookies_list)):
			self.cookies_list[i]['sameSite'] = 'Strict'
		return self.cookies_list