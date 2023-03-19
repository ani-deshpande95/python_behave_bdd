
from selenium import webdriver


def go_to(url, browser_type=None):
    if not browser_type:
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception("Incorrect browser type")

    driver.get(url)
    driver.maximize_window()
    return driver


def find_element(context, element_identifier, element_locator):
    element_identifiers = ["id", "link text", "partial link text", "css selector", "xpath", "name", "tag name"]

    if element_identifier not in element_identifiers:
        raise Exception("Element Identifier is incorrect")

    web_element = context.driver.find_element(element_identifier, element_locator)

    return web_element
