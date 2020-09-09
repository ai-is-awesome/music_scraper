
from requests_module import Request
from bs4 import BeautifulSoup
bs = BeautifulSoup
import bs4


def get_resp(url):
    resp = Request.get(url)
    return resp


def get_soup(url):
    resp = get_resp(url)
    soup = bs(resp.text, 'lxml')

    return soup


def clean_text(text):
    return text.strip(' ').replace('\n', '').replace('\t', '').replace('\r', '')


def is_text_in_tag(tag, text):
    if type(tag) == bs4.element.ResultSet:
        for t in tag:
            if text in t.text:
                return t
    else:
        if text in tag.text:
            return tag
        


def get_details(urlorsoup):
    if type(urlorsoup) == str:
        soup = get_soup(urlorsoup)
    else:
        soup = urlorsoup
    


    D = dict()
    product = soup.find('div', class_ = 'col-product-detail')
    D['series'] = is_text_in_tag(product.find_all('span'), 'Series:').text.replace('Series:', '') if is_text_in_tag(product.find_all('span'), 'Series:') else None
    D['publisher'] = is_text_in_tag(soup.find_all('span'), 'Publisher: ').text.replace('Publisher', '') if is_text_in_tag(product.find_all('span'), 'Publisher:') else None
    D['format'] = is_text_in_tag(soup.find_all('span'), 'Format').text.replace('Format:', '') if is_text_in_tag(product.find_all('span'), 'Format:') else None
    temp = soup.find('div', class_ = 'col-product-detail-content')
    D['details'] = temp.text if temp else None
    
            
    
    for key in D.keys():
        if D[key]:
            D[key] = clean_text(D[key])
    return D





test_url = 'https://www.halleonard.com/product/296761/all-in-one-piano-lessons-book-a?subsiteid=1'



