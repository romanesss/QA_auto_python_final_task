from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    GO_TO_BASKET_FROM_HOME = (By.CSS_SELECTOR, ".btn-group [class='btn btn-default']")
    EMPTY_BASKET = (By.CSS_SELECTOR,"#content_inner")
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, "[class='basket-items']")

class MainPageLocators():
    pass

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    #селекторы полей формы логина
    #LOGIN_LOGIN = (By.CSS_SELECTOR,    "#id_login-username")
    #LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    #селекторы полей формы регистрации
    #LOGIN_REGISTRATION = (By.CSS_SELECTOR,    "#id_registration-email")
    #PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    #CONFIRM_PASSWORD = (By.CSS_SELECTOR,      "#id_registration-password2")

class ProductPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR,                   "[class='btn btn-lg btn-primary btn-add-to-basket']")
    TRUE_NAME_PRODUCT = (By.CSS_SELECTOR,               "h1:nth-child(1)")
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR,            "[class='alert alert-safe alert-noicon alert-success  fade in'] strong")
    ALLERT_MESSAGE = (By.CSS_SELECTOR,                  "[class='alert alert-safe alert-noicon alert-success  fade in']")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR,         "[class='alertinner '] p:nth-child(1)")
    TRUE_PRISE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR,    "[class='price_color']")
    PRISE_PRODUCT_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "[class='alertinner '] p:nth-child(1) strong")