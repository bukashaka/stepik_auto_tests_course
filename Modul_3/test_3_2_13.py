import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Заполняем обязательные поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input").send_keys("ivan.petrov@example.com")

        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ждём перехода
        time.sleep(1)

        # Проверяем успешную регистрацию
        success_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations!", success_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Заполняем обязательные поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input").send_keys("ivan.petrov@example.com")

        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ждём перехода
        time.sleep(1)

        # Проверяем успешную регистрацию
        success_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations!", success_text)

if __name__ == "__main__":
    unittest.main()
