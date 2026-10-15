import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url



def test_google_web(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert "Google" in driver.title
    assert driver.current_url.startswith("https://www.google.com")



def test_github_web(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert driver.current_url.startswith("https://github.com")