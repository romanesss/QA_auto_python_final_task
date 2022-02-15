from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import pytest

# links for parammetrize
'---------------------------------------------------------------------------------------'
f = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
s = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
t = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
fo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
fi = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"
six = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
sev = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
eig = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
nine = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
ten = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
'---------------------------------------------------------------------------------------'


@pytest.mark.parametrize('link', [f, s, t, fo, fi, six, sev, pytest.param(eig, marks=pytest.mark.skip), nine, ten])
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


def test_guest_can_see_success_message(browser):
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