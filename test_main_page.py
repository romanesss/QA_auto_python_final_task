import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.test_product_page import ProductPage

def test_guest_can_go_to_login_page(browser) :
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open(browser,link)
    page.go_to_login_page()


def test_guest_should_see_login_link(browser) :
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open(browser, link)
    page.should_be_login_link()

def test_login_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open(browser, link)
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open(browser, link)
    page.should_be_login_form()

def test_guest_should_see_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open(browser, link)
    page.should_be_register_form()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open(browser,link)
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.visible_allert_message()
    page.check_right_product_name()
    page.visible_add_to_basket_message()
    page.check_right_product_prise()

    #time.sleep(10000)