import time
import json
from playwright.sync_api import sync_playwright


with open("cookies.json", 'r') as file:
    cookies = json.load(file)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.clear_cookies()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    context.add_cookies(cookies)

    search_window = page.get_by_placeholder("Введите запрос")
    search_window.click()
    time.sleep(1)
    search_window.fill("иван золо")
    time.sleep(1)
    search_window.press("Enter")
    time.sleep(5)
    page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[6]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click(click_count=3)
    time.sleep(5)
    like_button = page.locator('xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    like_button.dblclick()
    like_button.press("Enter")
    time.sleep(5)
    subscribe_button = page.locator("xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-smartimation/yt-button-shape/button")
    subscribe_button.dblclick()
    subscribe_button.press("Enter")
    time.sleep(140)
