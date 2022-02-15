import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest

# links for parammetrize
'---------------------------------------------------------------------------------------'
parametrs = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
'---------------------------------------------------------------------------------------'

@pytest.mark.parametrize('link', parametrs)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.visible_allert_message()
    page.check_right_product_name()
    page.visible_add_to_basket_message()
    page.check_right_product_prise()

'''--------------------negative_tests--------------------'''
@pytest.mark.skip
def test_guest_can_see_success_message_after_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.go_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.go_to_basket()
    page.should_not_dissapeared_be_message()
"""------------------------------------------------------------"""

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open(browser, link)
    page.go_to_basket_page()
    page.empty_basket_text()
    "-------Negative-------"
    page.empty_basket_list()
    "----------------------"

class TestUserAddToBasketFromProdutPage():
    @pytest.fixture(scope='function',autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open(browser, link)
        ##register of fake user
        self.page.register_new_user(str(time.time()) + '@fakemail.org', "qwertyuiop123456789")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open(browser, link)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open(browser, link)
        page.go_to_basket()
        page.visible_allert_message()
        page.check_right_product_name()
        page.visible_add_to_basket_message()
        page.check_right_product_prise()