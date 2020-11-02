import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(1)
    request.addfinalizer(wd.quit)
    return wd


def login(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


def test_new_tabs(driver):
    login(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("#content > div > a").click()
    links = driver.find_elements_by_css_selector("td > a[href*='http']")
    for i in links:
        countries_window = driver.current_window_handle
        all_windows_before_open_i = driver.window_handles
        i.click()
        wait = WebDriverWait(driver, 10)
        new_window = wait.until(NewWindowIsOpen(driver, all_windows_before_open_i))
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(countries_window)


class NewWindowIsOpen:
    def __init__(self, driver, all_windows_before_open_i):
        self._driver = driver
        self._all_windows_before_open_i = all_windows_before_open_i

    def __call__(self, driver):
        all_windows_after_open_i = driver.window_handles
        new_window = None
        for i in self._all_windows_before_open_i:
            for k in all_windows_after_open_i:
                if i != k:
                    new_window = k
                    break
        if new_window == '':
            return False
        else:
            return new_window
