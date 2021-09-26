from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_allert(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.solve_quiz_and_get_code()
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket
