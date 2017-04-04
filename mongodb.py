import requests
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
bnb_info = xiaozhu['bnb_info']

# ====================================================== <<<< 单页行为 >>>> =============================================

url = 'http://bj.xiaozhu.com/search-duanzufang-p20-0/'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('span.result_title')
prices = soup.select('span.result_price > i')

for title, price in zip(titles,prices):
    data = {
        'title':title.get_text(),
        'price':int(price.get_text())
    }
    bnb_info.insert_one(data)
print('Done')

# ====================================================== <<<< 设计函数 >>>> =============================================

def get_page_within(pages):
    for page_num in range(1,pages+1):
        wb_data = requests.get('http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('span.result_title')
        prices = soup.select('span.result_price > i')
        for title, price in zip(titles,prices):
            data = {
                'title':title.get_text(),
                'price':int(price.get_text())
            }
            bnb_info.insert_one(data)
    print('Done')

# get_page_within(3) 获取前三页面得数据


# 从数据库中进行筛选
# for i in bnb_info.find():
#     if i['price'] >= 500:
#         print(i)

# client = pymongo.MongoClient('localhost',27017)
# walden = client['walden']
# sheet_tab = walden['sheet_tab']

# path = '/Users/Hou/Desktop/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             'index':index,
#             'line' :line,
#             'words':len(line.split())
#         }
#         sheet_tab.insert_one(data)

# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
# for item in sheet_tab.find({'words':{'$lt':5}}):
#     print(item)
