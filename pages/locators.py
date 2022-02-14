from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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