from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

    def get_category_html(category):
    raw_html = simple_get('https://www.indonetwork.co.id/' + category + '/perusahaan?page=2')
    html = BeautifulSoup(raw_html, 'html.parser')

    return html

html = get_category_html('komputer-dan-laptop')
companies = html.find_all(class_='product-info')
findCompanies = browser.find_elements_by_class_name('product-info')
for company in findCompanies:
    company.find_element_by_class_name('mask-phone-button').click()
for company in companies:
    company_name = company.find(class_='link_product').text.replace('\n',' ').replace('          ','').replace(' ','',1)
    if company.find('div', class_='rubymember') is not None:
        company_level = 'Premium Ruby'
    elif company.find('div', class_='blueonyxmember') is not None:
        company_level = 'Premium Blue Onyx'
    elif company.find('div', class_='goldmember') is not None:
        company_level = 'Premium Gold'
    else:
        company_level = 'Free'
    company_address = company.find(class_='seller-name').text.replace('\n',' ').replace('Alamat','').replace(':','').replace(' ','', 4).replace('&nbsp','')
    company_telephone = company.find(class_='nowa').text.replace('\n',' \\ ')

    print(f'''
    Company Name\t: {company_name}
    Level\t\t: {company_level}
    Address\t\t: {company_address}
    Phone Number\t: {company_telephone}
    '''
    )