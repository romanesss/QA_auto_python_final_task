from pages.locators import BasketPageLocators
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def go_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def check_right_product_name(self):
        true_product_name = self.browser.find_element(*ProductPageLocators.TRUE_NAME_PRODUCT)
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT)
        assert true_product_name.text == message_product_name.text ,\
            "*** Product name in message not true!!! ***"

    def visible_allert_message(self):
        assert self.is_element_present(*ProductPageLocators.ALLERT_MESSAGE),\
            "*** No allert message!!! ***"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALLERT_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_dissapeared_be_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALLERT_MESSAGE),\
            "*** Success message is not disappeared !!! ***"

    def visible_add_to_basket_message(self):
        assert  self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE),\
            "*** No add to basket message!!! ***"

    def check_right_product_prise(self):
        prise_in_message = self.browser.find_element(*ProductPageLocators.PRISE_PRODUCT_IN_BASKET_MESSAGE)
        true_prise = self.browser.find_element(*ProductPageLocators.TRUE_PRISE_PRODUCT_IN_BASKET)
        assert  prise_in_message.text == true_prise.text ,\
            "*** Prise of product not true!!! ***"