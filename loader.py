from playwright.sync_api import sync_playwright
from cookies_json_functions import LoadJson, ChangeSameSiteInCookie
from playwright_func_class import PlaywrightFunctions


def load_cookies():
	load_json = LoadJson("cookies.json")
	cookies_list = load_json.load_json()
	change_same_site = ChangeSameSiteInCookie(cookies_list)
	cookies_list = change_same_site.change_same_site_value()
	return cookies_list


def run_playwright_functions():
	with sync_playwright() as pw:
		pw_functions = PlaywrightFunctions(pw)
		pw_functions.like_and_subscribe_to_sixth_video_in_search_query("Иван золо", load_cookies())
		pw_functions.close_browser_page()


run_playwright_functions()