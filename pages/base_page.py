from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, locator):
        self.find_clickable_element(locator).click()

    def add_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])