from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# переход на нужную страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# находим все нужные элементы на странице
name_field = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
lastname_field = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
email_field = browser.find_element(By.CSS_SELECTOR, "[name='email']")
file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
send_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

# заполняем форму
name_field.send_keys("H")
lastname_field.send_keys("F")
email_field.send_keys("y")

# создаём путь до файла test_file.txt в текущей папке
current_dir = os.path.abspath(os.path.dirname(__file__))  # путь к текущей папке
file_path = os.path.join(current_dir, "../lesson3/test_file.txt")

# если файла ещё нет — создаём временно
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("Hello, this is test file!")

# загружаем файл
file_button.send_keys(file_path)

# отправляем форму
send_button.click()

# ждём, чтобы увидеть результат (например, код)
time.sleep(5)
browser.quit()
