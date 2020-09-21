from bs4 import BeautifulSoup

local_path = 'c:/users/piyush/desktop/'

def save_soup(soup_or_resp):
    '''
    Helper function for debugging
    '''
    import requests
    if type(soup_or_resp) == requests.models.Response:
        soup = BeautifulSoup(soup_or_resp.text, 'lxml')
    
    else:
        soup = soup_or_resp
    
        
    with open(local_path + 'soup.html', 'w', encoding = 'utf-8') as file:
        file.write(str(soup))


