from pom.base import WebPage
from pom.elements import WebElement


class ShopingCart(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://lascana.ru/'
        super().__init__(web_driver, url)

    cookies = WebElement(css_selector='body > div.cookie-popup > div')
    clothes_tab = WebElement(css_selector='li.navigation-menu__item:nth-child(3)')
    first_picture = WebElement(xpath='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
    uniq_product_article = WebElement(id='product__article')
    # discount_window = WebElement(css_selector='.discounts-popup')
    button_add_to_cart = WebElement(css_selector='#bx_117848907_9787_add_basket_link')
    go_to_cart = WebElement(id='go-to-cart__button-cart')
    picture_product_in_the_cart = WebElement(css_selector='.cart__item--image')