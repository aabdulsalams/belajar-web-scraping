from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Safari()
browser = webdriver.Chrome('/Users/abdulsalam/Documents/dll/chromedriver')
keyword = 'komputer'
browser.get('https://www.indonetwork.co.id/showcase/'+keyword)

# browser.get('https://www.indonetwork.co.id')
# searchKeyword = browser.find_element_by_name('q')
# searchKeyword.send_keys('coba')
# searchKeyword.send_keys(Keys.RETURN)

findCompanies = browser.find_elements_by_class_name('product-info')
for company in findCompanies:
    company.find_element_by_class_name('mask-phone-button').click()
    company_name = company.find_element_by_tag_name('h3').text.replace('\n',' ')
    company_location = company.find_element_by_id('lokasi').text.replace('•','\\')
    company_address = company.find_element_by_class_name('seller-name').text.replace('\n',' ').replace('Alamat','').replace(':','').replace(' ','',2)
    company_telephone = company.find_element_by_class_name('nowa').text.replace('\n',' \\ ')
    print(f'''
    Company Name\t: {company_name}
    City \ Province\t: {company_location}
    Address\t\t: {company_address}
    Telephone Number\t: {company_telephone}
    '''
    )