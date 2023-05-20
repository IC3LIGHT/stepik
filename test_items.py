import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_button_shopping_cart(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket .btn")
    assert button, "The button not found"
