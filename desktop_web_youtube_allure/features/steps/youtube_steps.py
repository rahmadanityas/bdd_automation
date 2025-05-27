from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

@given('the browser is open')
def step_open_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=options)

@when('the user navigates to YouTube')
def step_navigate_youtube(context):
    with allure.step("Navigating to YouTube"):
        context.driver.get("https://www.youtube.com")
        time.sleep(3)

@when('the user searches for "IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput"')
def step_search_video(context):
    with allure.step("Searching for video"):
        search_box = context.driver.find_element(By.NAME, "search_query")
        search_box.send_keys("IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

@when('the user opens the video titled "IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput"')
def step_open_video(context):
    with allure.step("Opening the specific video"):
        results = context.driver.find_elements(By.ID, "video-title")
        for result in results:
            if "IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput" in result.get_attribute("title"):
                result.click()
                time.sleep(5)  # wait for video to load
                context.video_opened = True
                return
        assert False, "Expected video not found to click."

@when('the user skips the ad if present')
def step_skip_ad(context):
    with allure.step("Checking and skipping ad if present"):
        try:
            wait = WebDriverWait(context.driver, 10)
            skip_btn = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button"))
            )
            skip_btn.click()
            print("⏩ Ad skipped.")
            time.sleep(2)
        except Exception as e:
            print("No skippable ad found or already skipped.")

@then('the video is playing')
def step_video_is_playing(context):
    with allure.step("Checking if video is playing"):
        current_url = context.driver.current_url
        assert "youtube.com/watch" in current_url, "The video URL is incorrect or video didn't open."
        print(f"\n🎬 Video is playing at URL: {current_url}")
        context.driver.quit()
