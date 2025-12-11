import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    return webdriver.Chrome()


def test_title_name(driver):
    driver.get("http://localhost:4000/labelPage")
    time.sleep(0.5)

    city_label = driver.find_element(By.ID, "city")
    city = city_label.text
    assert city == "Dundalk"

    driver.close()


def test_label_page(driver):
    driver.get("http://localhost:4000/labelPage")
    time.sleep(0.5)

    county_label = driver.find_element(By.ID, "county")
    county = county_label.text
    assert county == "Louth"

    driver.close()


def test_enter_data(driver):
    driver.get("http://localhost:4000/labelPage")
    time.sleep(0.5)

    country_label = driver.find_element(By.ID, "country")
    country = country_label.text
    assert country == "Ireland"

    driver.close()
