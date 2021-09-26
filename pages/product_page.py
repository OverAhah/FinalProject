from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_basket(self):
        self.should_be_msg
        self.should_be_product_name
        self.should_be_prise

    def should_be_msg(self):
        assert self.browser.find_element(*ProductPageLocators.MSG_FORM), "Message is not presented!"

    def should_be_product_name(self):
        assert  self.browser.find_element(*ProductPageLocators.ASSERT_BOOK_NAME) in self.browser.find_element(*ProductPageLocators.BOOK_NAME), "Book name is different!"

    def should_be_prise(self):
        assert  self.browser.find_element(*ProductPageLocators.ASSERT_PRICE) in self.browser.find_element(*ProductPageLocators.PRiCE), "Price is different!"
