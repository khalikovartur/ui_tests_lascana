import pytest
from pom.smoke_regis_auth import AuthPage
import time

def test_authentification_user(web_browser):
    """Authentification with existing user data """

    user_name = 'Алла'
    e_mail ='alla@mail.com'
    password ='alla1234'
    
    page = AuthPage(web_browser)
    page.user_icon.click()
    page.email.send_keys(e_mail)
    page.password.send_keys(password)
    page.auth_submit_button.click()
    time.sleep(2)
    
    name_header = page.name_header_link.get_text()
    assert name_header == user_name 
    
    