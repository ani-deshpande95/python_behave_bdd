from selenium import webdriver


def go_to_url(url, browser_type=None):
    if not browser_type:
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception("Incorrect browser type")

    driver.get(url)

    return driver
