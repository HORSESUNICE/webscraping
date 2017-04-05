from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re

driver=webdriver.Chrome()
driver.get('https://www.zhihu.com/question/35768596')

# 模拟点击更多
try:
    while True:
        time.sleep(2)
        more=driver.find_element_by_xpath('//div[@class="Card"]/button')
        more.click()
except NoSuchElementException:
    pass

page_source=driver.page_source
# print(page_source)
# soup=BeautifulSoup(page_source,'html.parser')
soup=BeautifulSoup(page_source,'lxml')

# 所有回答
mainpage = soup.find('div', attrs={'id': 'root'}).find('div', attrs={'class': 'Question-main'})
# 单个回答找到每个回答
items = mainpage.find_all('div', attrs={'class': 'List-item'})
# 第三步， 迭代每个回答获取到需要的数据
for item in items:
    imgs = item.find_all('noscript')
    for img in imgs:
        # re解析url
        print(re.findall(r"src=\"(.+?)\"",img.text)[0])