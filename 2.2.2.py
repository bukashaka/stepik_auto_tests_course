from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение x
    x_value = browser.find_element(By.ID, "input_value").text
    answer = calc(x_value)

    # Прокручиваем страницу до поля ввода
    input_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", input_field)

    # Вводим ответ
    input_field.send_keys(answer)

    # Ставим галочку и радиокнопку
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # Скроллим к кнопке и нажимаем её
    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", send_button)
    send_button.click()

    # Пауза, чтобы увидеть результат
    time.sleep(5)

finally:
    browser.quit()
