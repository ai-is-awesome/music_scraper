# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 05:29:55 2020

@author: Piyush
"""


from bs4 import BeautifulSoup
bs = BeautifulSoup
from requests_module import Request
from cookie_loader import get_cookies


cj = get_cookies()
def get_soup_from_url(url):
    r = Request.get(url, cookies = cj)
    soup = bs(r.text, 'lxml')
    return soup





def get_map_price(url):
    soup = get_soup_from_url(url)
    
    D = {'map_price' : None}
    prices = soup.find('div', class_ = 'wrap_price_map')
    if not prices:
        return D
    
    for price_div in prices.find_all('div'):
        if price_div.text and 'MAP' in price_div.text:
            D['map_price'] = price_div.text.replace('MAP: ', '')
            
    return D



test_url = ''




