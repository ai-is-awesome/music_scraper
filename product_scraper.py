# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:16:40 2020

@author: Piyush
"""

import pandas as pd
from bs4 import BeautifulSoup
bs = BeautifulSoup
from requests_module import Request

PRODCUTS_FILE_READ_LOCATION = ''
PRODUCTS_FILE_SAVE_LOCATION = ''




def get_df(location):
    df = pd.read_csv(location)
    return df



def get_description(soup):
    product_bullet_scroll_div = soup.find('div', attrs = {'id' : 'product_bullet_scroll'})
    start = 1
    string = ''
    for li in product_bullet_scroll_div.find_all('li'):
        string += '(' + str(start) + ') ' + li.text + '. '
        start += 1
        
    return string



def get_resp(url):
    return Request.get(url)


def get_soup(resp):
    return BeautifulSoup(resp.text, 'lxml')




def get_image_details(soup):
    D = dict()
    cont = soup.find('div', attrs = {'id' : 'productView_container_bd'})
    count = 1
    for img in cont.find_all('img'):
        if img.get('title') and img.get('title').startswith('Product Image:'):
            string = 'image_link_' + str(count)
            url = 'https://www.tmppro.com' + img.get('src')
            D[string] = url
            count+= 1
            
    return D
    


def get_product_details(urlorsoup):
    if type(urlorsoup) == str:
        r = get_resp(urlorsoup)
        soup = get_soup(r)
        
    else:
        soup = urlorsoup
    
    image_details = get_image_details(soup)    
    cls = 'productView_longDesc_box'
    
    
    D = {'Brand Name' : None, 
         'Model Number:' : None, 
         'TMP Item #:' : None,
         'Series Name:' : None, 
         'UPC / EAN:' : None, 
         'Namm Category Name:': None, 
         'List:' : None, 'Short Description:' : None,
         'description' : None, 'invoice_number' : None, 
         'image_link' : None, }
    
    details_sec = soup.find('div', class_ = 'descSectiontwo descSection').find('div', class_ = cls)
    
    L = ['Brand Name', 'Model Number:', 'TMP Item #:', 'Series Name:', 'UPC / EAN:', 'Namm Category Name:', 'List:', 'Short Description:', ]
    
    for detail_title in details_sec.find_all('div', class_ =  'productDetail'):
        if detail_title.text in L:
            detail_title_value = detail_title.findNext('div', class_ = 'productDetail_text').text if detail_title.findNext('div', class_ = 'productDetail_text') else None
            D[detail_title.text] = detail_title_value
    
         
    D['description'] = get_description(soup)
    D['invoice_number'] = soup.find('div', class_ = 'wrap_price_inv').text
    

    D.update(image_details.copy())
    return D
         