def test_open_main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    assert "Самокат" in driver.title