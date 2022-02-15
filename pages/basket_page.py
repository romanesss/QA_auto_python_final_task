from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text == "Your basket is empty. Continue shopping" ,\
            "*** Basket not empty!!! ***"
    def empty_basket_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST),\
            "*** Basket have some product!!! ***"