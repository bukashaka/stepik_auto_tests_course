from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip
import time

# функция, которая находит значение выражения при заданном x
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

# переход на нужную страницу
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # кликаем по волшебной кнопке
    magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    magic_button.click()

    # принимаем alert
    alert = browser.switch_to.alert
    alert.accept()

    # находим значение x для выполнения задания
    x_string = browser.find_element(By.ID, "input_value")
    x_number = int(x_string.text)

    # считаем ответ
    answer = calc(x_number)

    # вводим ответ
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer)

    # нажимаем кнопку
    send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    send_button.click()

    # ждем второй alert и копируем текст в буфер
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    result = alert_text.split(": ")[-1]
    pyperclip.copy(result)
    print("Скопировано в буфер обмена:", result)

finally:
    time.sleep(3)
    browser.quit()
