from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "Home_SubHeader__zwi_E")
    ORDER_BUTTON_TOP = (By.XPATH,".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH,".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    QUESTION_BY_ID = lambda index: (By.ID,f"accordion__heading-{index}")
    ANSWER_BY_ID = lambda index: (By.ID,f"accordion__panel-{index}")
    SCOOTER_LOGO = (By.XPATH,".//a[.//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH,".//a[.//img[@alt='Yandex']]")

class OrderPageLocators:

    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    METRO_STATION = lambda station_name: (By.XPATH,f".//div[text()='{station_name}']")

    DELIVERY_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_DAY = lambda day: (By.XPATH, f".//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month')) and text()='{day}']")
    
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = lambda period: (By.XPATH, f".//div[@class='Dropdown-option' and text()='{period}']")

    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, ".//button[text()='Назад']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    ORDER_CONFIRM_MODAL = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    CANCEL_ORDER_BUTTON = (By.XPATH, ".//button[text()='Нет']")

    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[text()='Заказ оформлен']")
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")