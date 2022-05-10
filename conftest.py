import pytest
import time
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('mironova-1993@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('ljvgbnjvwf')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   images = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
   names = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-title')))
   descriptions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-text')))

def test_all_pets():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    time.sleep(10)

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

