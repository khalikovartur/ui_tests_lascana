import pytest
from pom.adding_to_shopping_cart import ShoppingCart


def test_adding_into_shopping_cart(web_browser):
    """Add to the shopping cart and go to the shopping cart page to check it"""

    page = ShoppingCart(web_browser)

    page.clothes_tab.click()
    page.first_product_picture.click()
    page.cookies.delete()

    # Getting the unique article of product
    product_article = page.uniq_product_article.get_text()
    page.button_add_to_cart.click()
    page.go_to_cart.click()

    # Go to shopping cart page
    current_url = page.get_current_url()
    assert current_url == "https://lascana.ru/personal/cart/"

    # Checking product unique article in the shopping cart
    page.picture_product_in_the_cart.click()
    assert product_article == page.uniq_product_article.get_text()
