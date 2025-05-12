import os
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def login_stepik(browser):
    login = os.getenv("STEPIC_LOGIN")
    password = os.getenv("STEPIC_PASSWORD")
    assert login and password, "STEPIC_LOGIN и STEPIC_PASSWORD должны быть заданы как переменные окружения"

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login"))
    )
    login_button.click()

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email"))
    )
    email_input.send_keys(login)

    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)

    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    # Ждём исчезновения формы логина
    WebDriverWait(browser, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "sign-form"))
    )


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_submit_correct_answer(browser, link):
    browser.get(link)

    login_stepik(browser)

    # Рассчитываем ответ
    answer = str(math.log(int(time.time())))

    # Находим поле для ответа и вводим
    textarea = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    textarea.clear()
    textarea.send_keys(answer)

    # Кликаем на кнопку "Отправить"
    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    submit_btn.click()

    # Ждём появления фидбека
    feedback = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    result_text = feedback.text
    assert result_text == "Correct!", f"Неверный фидбек на {link}: '{result_text}'"
