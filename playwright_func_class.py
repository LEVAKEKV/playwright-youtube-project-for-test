import time
from playwright.sync_api import Playwright, sync_playwright


class PlaywrightFunctions():
	def __init__(self, playwright: Playwright) -> None:
		"""Инициализируем объекты и работаем с Playwright"""
		self.browser = playwright.chromium.launch(headless=False)
		self.context = self.browser.new_context()
		self.context.clear_cookies()
		self.page = self.context.new_page()

	def search_query(self, search_text: str, cookies: list[dict]) -> None:
		"""Функция для поиска запроса"""
		self.page.goto("https://www.youtube.com/")
		self.context.add_cookies(cookies)
		self.page.reload()
		search_window = self.page.get_by_placeholder("Введите запрос")
		search_window.click()
		time.sleep(1)
		search_window.fill(search_text)
		time.sleep(1)
		search_window.press("Enter")

	def open_sixth_video(self):
		"""Функция открытия шестого видео"""
		sixth_video_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-t"
											   "wo-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/y"
											   "td-item-section-renderer/div[3]/ytd-video-renderer[6]/div[1]/div/div[1]/"
											   "div/h3/a/yt-formatted-string")
		sixth_video_button.dblclick()
		time.sleep(5)

	def click_like_button(self):
		"""Функция для нажатия на кнопку лайка"""
		like_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/"
										"div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1"
										"]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-tog"
										"gle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
		like_button.dblclick()
		like_button.press("Enter")
		time.sleep(1)

	def click_subscribe_button(self):
		"""Функция для нажатия на кнопку подписки"""
		subscribe_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/di"
											 "v[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-but"
											 "ton-renderer/yt-smartimation/yt-button-shape/button")
		subscribe_button.dblclick()
		subscribe_button.press("Enter")
		time.sleep(1)


	def close_browser_page(self):
		"""Функция для закрытия страницы браузера"""
		self.context.close()
		self.browser.close()