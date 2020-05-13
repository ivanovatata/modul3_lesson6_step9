import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_dd_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(30)

    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "There is not element 'Add to cart' on the page"

