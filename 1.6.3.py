from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все input-элементы на странице
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Вводим короткий текст в каждое поле
    for element in elements:
        element.send_keys("Тест")

    # Находим и нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем увидеть результат
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Пустая строка в конце файла