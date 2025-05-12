# Тут расположено решение тестового задания по курсу
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 3, 6 степ

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import math
import time

# функция, которая находит значение выражения при заданном x
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

# переход на нужную страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # нажимаем на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    # переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # находим значение x для выполнения задания
    x_string = browser.find_element(By.ID, "input_value")
    x_number = int(x_string.text)

    # высчитываем результат для задания
    answer = calc(x_number)

    # вводим ответ к тесту
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer)

    # нажимаем на кнопку
    send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    send_button.click()

    # подождем немного появления alert
    time.sleep(1)

    # переключаемся на alert, достаем текст алерта
    alert = browser.switch_to.alert
    alert_text = alert.text

    # достаем из текста алерта число, копируем в буфер обмена
    result = alert_text.split(": ")[-1]
    print("Результат:", result)
    pyperclip.copy(result)

finally:
    # даем время, чтобы скопировать результат вручную (если что)
    time.sleep(5)
    browser.quit()
