import allure

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    MAIN_URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(self.MAIN_URL)

    @allure.step("Кликнуть по верхней кнопке заказа")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть по нижней кнопке заказа")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Раскрыть вопрос FAQ с индексом: {index}")
    def click_question_by_index(self, index):
        locator = MainPageLocators.QUESTION_BY_ID(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить текст ответа FAQ с индексом: {index}")
    def get_answer_text_by_index(self, index):
        return self.get_text(MainPageLocators.ANSWER_BY_ID(index))

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
