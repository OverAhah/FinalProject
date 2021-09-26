from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MSG_FORM = (By.CSS_SELECTOR, "div#messages")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRiCE = (By.CSS_SELECTOR, "p.price_color")
    ASSERT_BOOK_NAME = (By.CSS_SELECTOR, "div#messages div.alert-success :nth-child(2) :nth-child(1)")
    ASSERT_PRICE = (By.CSS_SELECTOR, "div.alert-info div.alertinner :nth-child(1) :nth-child(1)")
