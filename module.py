from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

class Site:
    def __init__(self, browser_name, url, chromedriver_path=None):
        self.driver = None
        try:
            if browser_name == "chrome":
                options = ChromeOptions()
                service = ChromeService(executable_path=chromedriver_path)
                self.driver = webdriver.Chrome(service=service, options=options)
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")

            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            if self.driver:
                self.driver.quit()
            raise e

    def get_element_property(self, method, selector, property_name):
        if method == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
        elif method == "xpath":
            element = self.driver.find_element(By.XPATH, selector)
        else:
            raise ValueError(f"Unsupported method: {method}")
        return element.value_of_css_property(property_name)

    def close(self):
        if self.driver:
            self.driver.quit()
