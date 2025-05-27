from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

@given("the Edge browser is open")
def step_open_edge_browser(context):
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Edge(options=options)

@when("the user opens the IDEMIA Line homepage")
def step_open_line_homepage(context):
    with allure.step("Opening IDEMIA Line homepage"):
        context.driver.get("https://theline.idemia.com/home/")
        time.sleep(3)

@when("the user navigates to the Global News Center")
def step_open_news_center(context):
    with allure.step("Clicking on Global News Center"):
        news_link = context.driver.find_element(By.LINK_TEXT, "Global News Center")
        news_link.click()
        time.sleep(3)

@when("the user searches for the IST news article")
def step_search_news_article(context):
    with allure.step("Typing the IST news article title in search input"):
        driver = context.driver
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-id="content-filter-keyword-filter"]'))
        )
        search_input.clear()
        search_input.send_keys("Discover the New IST Presentation – Now Available in English & French")


@when("the user applies the search filter")
def step_apply_search_filter(context):
    with allure.step("Clicking the apply filter button"):
        driver = context.driver

        # Dismiss GDPR if present
        try:
            gdpr_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="gdpr-accept"]'))
            )
            gdpr_button.click()
            time.sleep(1)
        except:
            pass  # No GDPR banner

        # Locate and scroll to Apply button
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="content-filter-button-submit"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", apply_button)
        time.sleep(0.5)
        apply_button.click()


@when("the user opens the article")
def step_click_article_link(context):
    with allure.step("Clicking the article link and switching to new tab"):
        driver = context.driver

        # Wait for the article link to be visible and clickable
        article_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-id="content-8470208776569657-content-title-link"]'))
        )

        # Scroll to make sure it's in view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", article_link)
        time.sleep(0.5)

        # Store current tab handle
        original_window = driver.current_window_handle
        current_tabs = driver.window_handles

        # Click the link
        article_link.click()

        # Wait for new tab to open
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > len(current_tabs)
        )

        # Switch to the new tab
        new_tabs = driver.window_handles
        for handle in new_tabs:
            if handle != original_window:
                driver.switch_to.window(handle)
                break

        # Optional: assert page URL
        WebDriverWait(driver, 10).until(
            EC.url_contains("New-IST-Presentation-Available")
        )


@then('the news article is displayed')
def step_news_is_displayed(context):
    current_url = context.driver.current_url
    print(f"Current URL: {current_url}")
    
     # Scroll gradually over 10 seconds
    scroll_pause_time = 2
    scroll_steps = 5  # 5 steps * 2 seconds = 10 seconds

    for _ in range(scroll_steps):
        context.driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
        time.sleep(scroll_pause_time)

    context.driver.quit()

