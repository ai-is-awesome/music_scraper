# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 04:54:55 2020

@author: Piyush
"""

from bs4 import BeautifulSoup
from requests_module import Request
from cookie_loader import get_cookies




#Make sure test_url has a map price
test_url = 'http://tmppro.com/products/view/217789/359151'


login_fail_text = 'OOPS! You\'re probably not logged in or cookies are not loaded \
properly. Make sure firefox is open and youre logged in and \
cookies are being loaded. '
              
login_pass_text = 'Test Successful. MAP keyword successfully detected. You\'re logged in.'


def test():
    cj = get_cookies()
    logged_in = False
    r= Request.get(test_url, cookies = cj)
    soup = BeautifulSoup(r.text, 'lxml')
    prices = soup.find('div', class_ = 'wrap_price_map')
    if not prices:
        print(login_fail_text)
        return
    
    
    for price_div in prices.find_all('div'):
        if price_div.text and 'MAP' in price_div.text:
            logged_in = True
            
    if logged_in:
        print(login_pass_text)
    
    else:
        print(login_fail_text)
        
        