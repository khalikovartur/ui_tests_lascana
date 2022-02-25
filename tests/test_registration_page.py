import pytest 
from pom.smoke_regis_auth import RegisPage


def test_registration_new_user(web_browser):
    """Registration new user. For successfully registration user input new user data in a test. """

    name = 'Алла'
    last_name = 'Аллова'
    e_mail = 'alla@email.com'
    password = 'alla1234'
    
    page = RegisPage(web_browser)
    page.user_icon.click()
    page.regis_link.click()
    page.cookies.delete()
    
    page.last_name.send_keys(last_name)
    page.name.send_keys(name)
    page.email.send_keys(e_mail)
    page.password.send_keys(password)
    page.confirm_password.send_keys(password) 
    
    page.agreement.scroll_to_element()  
    page.agreement_box.click()
    
    page.regis_button.scroll_to_element()
    page.regis_button.click()
    page.regis_button.click()
    
    current_url = page.get_current_url()
    assert current_url == "https://lascana.ru/auth/index.php"
    
    
    
    
 