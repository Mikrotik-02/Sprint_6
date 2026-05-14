import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Найти видимый элемент: {locator}")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        self.find_clickable_element(locator).click()

    @allure.step("Ввести текст в элемент: {locator}")
    def add_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проскроллить к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Проверить, что элемент отображается: {locator}")
    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
