from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    # Уникальные селекторы: по CSS-классам и структуре HTML
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input")
    email.send_keys("ivan.petrov@example.com")

    # Кнопка отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём загрузку страницы
    time.sleep(1)

    # Проверка результата
    success_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations!" in success_text

finally:
    # Немного подождать, чтобы увидеть результат
    time.sleep(5)
    browser.quit()

