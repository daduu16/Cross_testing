import pytest
import yaml
from module import Site
import re

# Load the YAML file
with open("tests423/testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture(scope="module")
def site():
    browser_name = testdata.get("browser")
    url = testdata.get("url")
    chromedriver_path = testdata.get("chromedriver_path")
    site_instance = Site(browser_name, url, chromedriver_path)
    yield site_instance
    site_instance.close()

def rgba_to_hex(rgba):
    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', rgba)
    if match:
        r, g, b = map(int, match.groups())
        return f'#{r:02x}{g:02x}{b:02x}'
    raise ValueError(f"Invalid RGBA color: {rgba}")

@pytest.mark.parametrize("logo, expected_width", [
    ("div.logo__icon", "300px")
])
def test_logo_width(site, logo, expected_width):
    assert site.get_element_property("css", logo, "width") == expected_width, "Test 1 fail"

@pytest.mark.parametrize("logo, expected_height", [
    ("div.logo__icon", "175px")
])
def test_logo_height(site, logo, expected_height):
    assert site.get_element_property("css", logo, "height") == expected_height, "Test 2 fail"

@pytest.mark.parametrize("login_form, expected_color", [
    ("div.login-form", "#ff0000")
])
def test_form_color(site, login_form, expected_color):
    actual_color = site.get_element_property("css", login_form, "background-color")
    actual_color_hex = rgba_to_hex(actual_color)
    assert actual_color_hex == expected_color, f"Test 3 fail: expected {expected_color} but got {actual_color_hex}"

@pytest.mark.parametrize("passdiv, expected_width", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[2]', "372px")
])
def test_pass_width(site, passdiv, expected_width):
    assert site.get_element_property("xpath", passdiv, "width") == expected_width, "Test 4 fail"

@pytest.mark.parametrize("passdiv, expected_height", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[2]', "40px")
])
def test_pass_height(site, passdiv, expected_height):
    assert site.get_element_property("xpath", passdiv, "height") == expected_height, "Test 5 fail"

@pytest.mark.parametrize("maildiv, expected_width", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[1]', "133.688px")
])
def test_email_width(site, maildiv, expected_width):
    assert site.get_element_property("xpath", maildiv, "width") == expected_width, "Test 6 fail"

@pytest.mark.parametrize("maildiv, expected_height", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[1]', "40px")
])
def test_email_height(site, maildiv, expected_height):
    assert site.get_element_property("xpath", maildiv, "height") == expected_height, "Test 7 fail"

@pytest.mark.parametrize("domain, expected_width", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[3]', "133.688px")
])
def test_domain_width(site, domain, expected_width):
    assert site.get_element_property("xpath", domain, "width") == expected_width, "Test 8 fail"

@pytest.mark.parametrize("domain, expected_height", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[1]/div[3]/div[3]', "40px")
])
def test_domain_height(site, domain, expected_height):
    assert site.get_element_property("xpath", domain, "height") == expected_height, "Test 9 fail"

@pytest.mark.parametrize("nextbtn, expected_font_family", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[2]/a', "sans-serif")
])
def test_font_family(site, nextbtn, expected_font_family):
    assert site.get_element_property("xpath", nextbtn, "font-family") == expected_font_family, "Test 10 fail"

@pytest.mark.parametrize("nextbtn, expected_font_size", [
    ('//*[@id="app"]/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/form/div[2]/a', "14.4px")
])
def test_font_size(site, nextbtn, expected_font_size):
    assert site.get_element_property("xpath", nextbtn, "font-size") == expected_font_size, "Test 11 fail"
