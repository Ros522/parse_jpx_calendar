from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def is_jpx_open(date=datetime.now()):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)

    driver.implicitly_wait(10)

    driver.get(f'http://www.jpx.co.jp/calendar/{date.strftime("%Y%m")}.html')

    selector = f'td.fc-day[data-date=\'{date.strftime("%Y-%m-%d")}\']'
    elm = driver.find_element_by_css_selector(selector)
    c = elm.get_attribute('class').split(' ')
    bg = elm.get_attribute('style')
    driver.close()
    driver.quit()
    if 'fc-sat' in c or 'fc-sun' in c:
        return False
    if 'background-color: rgb(239, 239, 239);' in bg:
        return False
    return True
