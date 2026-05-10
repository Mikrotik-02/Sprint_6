import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title("Проверка успешного заказа через верхнюю кнопку Заказать")
def test_order_scooter_from_top_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()

    main_page.click_top_order_button()

    order_page.fill_order_form(
        name="Иван",
        surname="Петров",
        address="Москва, улица Ленина, 1",
        phone="+79991234567",
        station="Черкизовская",
        day="20",
        period="сутки",
        color="black",
        comment="Позвонить за час"
    )

    assert order_page.is_order_successful()


@allure.title("Проверка успешного заказа через нижнюю кнопку Заказать")
def test_order_scooter_from_bottom_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()

    main_page.click_bottom_order_button()

    order_page.fill_order_form(
        name="Анна",
        surname="Смирнова",
        address="Москва, улица Пушкина, 10",
        phone="+79997654321",
        station="Сокольники",
        day="21",
        period="двое суток",
        color="grey",
        comment="Оставить у подъезда"
    )

    assert order_page.is_order_successful()