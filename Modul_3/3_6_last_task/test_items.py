from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # можно раскомментировать паузу, чтобы видеть визуально язык
    time.sleep(5)
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button.is_displayed(), "Кнопка добавления в корзину не найдена!"
