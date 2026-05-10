from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_customer_info(self, name, surname, address, phone):
        self.add_text(OrderPageLocators.NAME_INPUT, name)
        self.add_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.add_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.add_text(OrderPageLocators.PHONE_INPUT, phone)

    def select_metro_station(self, station_name):
        self.add_text(OrderPageLocators.METRO_INPUT, station_name)
        self.click_element(OrderPageLocators.METRO_STATION(station_name))

    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def select_delivery_date(self, day):
        self.click_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.click_element(OrderPageLocators.CALENDAR_DAY(day))

    def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_OPTION(period))

    def select_scooter_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)
        else:
            raise ValueError(f"Unknown scooter color: {color}")

    def add_comment(self, comment):
        self.add_text(OrderPageLocators.COMMENT_INPUT, comment)

    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def is_order_successful(self):
        return self.is_element_displayed(OrderPageLocators.ORDER_SUCCESS_MODAL)

    def fill_order_form(self, name, surname, address, phone, station, day, period, color, comment):
        self.fill_customer_info(name, surname, address, phone)
        self.select_metro_station(station)
        self.click_next_button()
        self.select_delivery_date(day)
        self.select_rental_period(period)
        self.select_scooter_color(color)
        self.add_comment(comment)
        self.click_order_button()
        self.confirm_order()