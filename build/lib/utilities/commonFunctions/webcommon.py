
from selenium import webdriver


def go_to(url, browser_type=None):
    if not browser_type:
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception("Incorrect browser type")

    driver.get(url)
    return driver


def find_element(context, element_identifier, element_locator):
    element_identifiers = ["id", "linkText", "css", "xpath", "name"]

    if element_identifier not in element_identifiers:
        raise Exception("Element Identifier is incorrect")

    web_element = context.driver.findElement(element_identifier, element_locator)

    return web_element
