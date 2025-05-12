from selenium import webdriver
from selenium.webdriver.common.by import By  # Добавлен импорт By
import math
import time

# Функция, которая находит значение выражения при заданном x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Переход на нужную страницу
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение x
    x_in_first_test = browser.find_element(By.ID, "input_value")
    x_value = x_in_first_test.text

    # Вычисляем результат
    first_test_result = calc(x_value)

    # Вводим ответ
    first_test_input = browser.find_element(By.ID, "answer")
    first_test_input.send_keys(first_test_result)

    # Выбираем checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()

    # Нажимаем кнопку отправить
    send_button = browser.find_element(By.CLASS_NAME, "btn-default")
    send_button.click()

    # Немного подождать, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрытие браузера
    browser.quit()
