from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

# просто создаем экземпляр браузера — без лишних настроек
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    # ждем, пока цена не станет 10000 RUR
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # читаем x, считаем значение
    x = int(browser.find_element(By.ID, "input_value").text)
    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()

    # ждем алерт и выводим его текст
    WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    print("Ответ из алерта:", alert.text)
    alert.accept()

finally:
    browser.quit()

