import pyautogui
import time
from behave import given, when, then

@given('I click the start menu')
def step_click_start_menu(context):
    pyautogui.press('win')
    time.sleep(2)

@when('I search for "Word"')
def step_search_word(context):
    pyautogui.write("Word", interval=0.1)
    time.sleep(2)

@when('I open Word')
def step_open_word(context):
    pyautogui.press('enter')
    time.sleep(5)

@then('I type "Hi I\'m Here :]"')
def step_type_message(context):
    pyautogui.write("Hi I'm Here :]", interval=0.1)
    time.sleep(2)
