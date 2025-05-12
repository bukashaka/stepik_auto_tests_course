from selenium import webdriver
from selenium.webdriver.common.by import By  # Добавлен импорт By
import math
import time

# Функция для вычисления значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент сундука и достаём значение атрибута valuex
    chest = browser.find_element(By.ID, "treasure")
    x_value = chest.get_attribute("valuex")

    # Вычисляем результат
    result = calc(x_value)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Ставим чекбокс и радиокнопку
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Кликаем кнопку "Submit"
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    # Немного подождать, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
