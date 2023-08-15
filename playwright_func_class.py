import time
from playwright.sync_api import Playwright, sync_playwright


class PlaywrightFunctions():
	def __init__(self, playwright: Playwright) -> None:
		"""Инициализируем объекты и работаем с Playwright"""
		self.browser = playwright.chromium.launch(headless=False)
		self.context = self.browser.new_context()
		self.context.clear_cookies()
		self.page = self.context.new_page()

	def like_and_subscribe_to_sixth_video_in_search_query(self, search_text: str, cookies: list[dict]) -> None:
		"""Главная функция для поиска запроса, выбора шестого видео, лайка и подписки на видео"""
		# Ищем в строке поиска текст нашего запроса
		self.page.goto("https://www.youtube.com/")
		self.context.add_cookies(cookies)
		self.page.reload()
		search_window = self.page.get_by_placeholder("Введите запрос")
		time.sleep(1)
		search_window.click()
		search_window.fill("иван золо")
		time.sleep(1)
		search_window.press("Enter")
		# Открываем шестое видео на странице поиска
		sixth_video_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-"
											   "two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/"
											   "ytd-item-section-renderer/div[3]/ytd-video-renderer[6]/div[1]/div/div[1]"
											   "/div/h3/a/yt-formatted-string")
		sixth_video_button.dblclick()
		time.sleep(5)
		# Нажимаем на кнопку лайка на странице
		like_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/"
										"div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1"
										"]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-tog"
										"gle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
		like_button.dblclick()
		like_button.press("Enter")
		time.sleep(1)

		# Нажимаем на кнопку подписки на странице
		subscrition_button = self.page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/"
											   "div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe"
											   "-button-renderer/yt-smartimation/yt-button-shape/button")
		subscrition_button.dblclick()
		subscrition_button.press("Enter")
		time.sleep(5)

	def close_browser_page(self):
		"""Функция для закрытия страницы браузера"""
		self.context.close()
		self.browser.close()