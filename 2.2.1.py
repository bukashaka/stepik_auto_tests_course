from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элементы с числами
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    # выбираем сумму в выпадающем списке
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(num1 + num2))

    # нажимаем на кнопку
    send_button = browser.find_element(By.CLASS_NAME, "btn-default")
    send_button.click()

    # подождать немного, чтобы увидеть результат (можно убрать в автотесте)
    time.sleep(5)

finally:
    browser.quit()