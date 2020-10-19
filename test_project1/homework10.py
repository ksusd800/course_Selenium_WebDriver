from selenium.webdriver.support.color import Color
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


# а) на главной странице и на странице товара совпадает текст названия товара
def test_name_product(driver):
    driver.get("http://localhost:8080/litecart")
    campaigns = driver.find_element_by_css_selector('#box-campaigns')
    product = campaigns.find_element_by_css_selector('li:nth-child(1)')
    main_name = product.find_element_by_css_selector('div.name').text  # Yellow Duck
    product.click()
    duck_name = driver.find_element_by_css_selector('#box-product h1').get_attribute('textContent')
    if main_name == duck_name:
        print('на главной странице и на странице товара совпадает текст названия товара')
    else:
        raise Exception()


# б) на главной странице и на странице товара совпадают цены (обычная и акционная)
def test_price(driver):
    driver.get("http://localhost:8080/litecart")
    campaigns = driver.find_element_by_css_selector('#box-campaigns')
    product = campaigns.find_element_by_css_selector('li:nth-child(1)')
    main_reg_price = product.find_element_by_css_selector('s').text  # $20
    main_camp_price = product.find_element_by_css_selector('strong').text  # $18
    product.click()
    duck_reg_price = driver.find_element_by_css_selector('#box-product s').get_attribute('textContent')
    duck_camp_price = driver.find_element_by_css_selector('#box-product strong').get_attribute('textContent')
    if main_reg_price == duck_reg_price and main_camp_price == duck_camp_price:
        print('на главной странице и на странице товара совпадают цены (обычная и акционная)')
    else:
        raise Exception()



# в) обычная цена зачёркнутая и серая
def test_color_regular_price(driver):
    driver.get("http://localhost:8080/litecart")
    campaigns = driver.find_element_by_css_selector('#box-campaigns')
    product = campaigns.find_element_by_css_selector('li:nth-child(1)')
    # главная страница:
    color_reg_price = product.find_element_by_css_selector('s').value_of_css_property('color')  # rgba(119, 119, 119, 1)
    line_reg_price = product.find_element_by_css_selector('s').value_of_css_property('text-decoration')  # line-through solid rgb(119, 119, 119)
    if (Color.from_string(color_reg_price).red == Color.from_string(color_reg_price).blue == Color.from_string(color_reg_price).green) and ("line-through" in line_reg_price):
        print('обычная цена зачёркнутая и серая (главная страница)')
    else:
        raise Exception()
    # карточка товара:
    product.click()
    color_reg_price = driver.find_element_by_css_selector('#box-product s').value_of_css_property('color')  # rgba(119, 119, 119, 1)
    line_reg_price = driver.find_element_by_css_selector('#box-product s').value_of_css_property('text-decoration')  # line-through solid rgb(119, 119, 119)
    if (Color.from_string(color_reg_price).red == Color.from_string(color_reg_price).blue == Color.from_string(color_reg_price).green) and ("line-through" in line_reg_price):
        print('обычная цена зачёркнутая и серая (карточка товара)')
    else:
        raise Exception()

# г) акционная жирная и красная
def test_color_camp_price(driver):
    driver.get("http://localhost:8080/litecart")
    campaigns = driver.find_element_by_css_selector('#box-campaigns')
    product = campaigns.find_element_by_css_selector('li:nth-child(1)')
    # главная страница:
    color_camp_price = product.find_element_by_css_selector('strong').value_of_css_property('color')  # rgba(204, 0, 0, 1)
    bold_camp_price = product.find_element_by_css_selector('strong').value_of_css_property('font-weight')  # 700 (больше или равно 700-считается жирным)
    if Color.from_string(color_camp_price).blue == 0 and Color.from_string(color_camp_price).green == 0 and int(bold_camp_price) >= 700:
        print('акционная цена жирная и красная (главная страница)')
    else:
        raise Exception()
    # карточка товара:
    product.click()
    color_camp_price = driver.find_element_by_css_selector('#box-product strong').value_of_css_property('color')  # rgba(204, 0, 0, 1)
    bold_camp_price = driver.find_element_by_css_selector('#box-product strong').value_of_css_property('font-weight')  # 700 (больше или равно 700-считается жирным)
    if Color.from_string(color_camp_price).blue == 0 and Color.from_string(color_camp_price).green == 0 and int(bold_camp_price) >= 700:
        print('акционная цена жирная и красная (карточка товара)')
    else:
        raise Exception()

# д) акционная цена крупнее, чем обычная
def test_size_prices(driver):
    driver.get("http://localhost:8080/litecart")
    campaigns = driver.find_element_by_css_selector('#box-campaigns')
    product = campaigns.find_element_by_css_selector('li:nth-child(1)')
    # главная страница:
    size_reg_price = product.find_element_by_css_selector('div.price-wrapper > s').value_of_css_property('font-size')  # 18px
    size_camp_price = product.find_element_by_css_selector('div.price-wrapper > strong').value_of_css_property('font-size')  # 14.4px
    if size_reg_price < size_camp_price:
        print(size_reg_price, size_camp_price, 'акционная цена крупнее, чем обычная (главная страница)')
    else:
        raise Exception()
    # карточка товара:
    product.click()
    size_reg_price = driver.find_element_by_css_selector('#box-product s').value_of_css_property('font-size')  # 22px
    size_camp_price = driver.find_element_by_css_selector('#box-product strong').value_of_css_property('font-size')  # 16px
    if size_reg_price < size_camp_price:
        print(size_reg_price, size_camp_price, 'акционная цена крупнее, чем обычная (карточка)')
    else:
        raise Exception()