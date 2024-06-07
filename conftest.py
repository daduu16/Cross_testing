import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from module import Site

# YAML dosyasını yükleyin
with open("tests423/testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture(scope="module")
def site():
    # ChromeDriver'ın yolunu belirtin
    chrome_service = ChromeService(executable_path='/path/to/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/path/to/chrome"  # Tarayıcı ikili dosyasının yolu
    
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    site_instance = Site(driver)
    yield site_instance
    site_instance.close()
    driver.quit()

@pytest.fixture()
def logo():
    return "div.logo__icon"

@pytest.fixture()
def login_form():
    return "div.login-form"

@pytest.fixture()
def passdiv():
    return "div.passdiv"

@pytest.fixture()
def maildiv():
    return "div.maildiv"

@pytest.fixture()
def domain():
    return "div.domain"

@pytest.fixture()
def nextbtn():
    return "div.nextbtn"

@pytest.fixture()
def expected_values():
    return {
        "logo_width": "300px",
        "logo_height": "175px",
        "login_form_color": "#ff0000",
        "passdiv_width": "372px",
        "passdiv_height": "40px",
        "maildiv_width": "133.688px",
        "maildiv_height": "40px",
        "domain_width": "133.688px",
        "domain_height": "40px",
        "nextbtn_font_family": "sans-serif",
        "nextbtn_font_size": "14.4px"
    }
