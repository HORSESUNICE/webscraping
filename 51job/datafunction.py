import requests
from bs4 import BeautifulSoup
import pymongo

client=pymongo.MongoClient('localhost',27017)
jobofdata=client['jobofdata']
dataurl=jobofdata['dataurl']

urls=['http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(str(i)) for i in range(1,3)]

def get_url(url):
    web=requests.get(url)
    web.encoding='gbk'
    soup=BeautifulSoup(web.text,'lxml')
    pageurls=soup.select('div.el > p.t1 > span > a')#50
    citys=soup.select('div.el > span.t3')#51
    salarys=soup.select('div.el > span.t4')#51
    companys=soup.select('div.el > span.t2 > a')#50
    for i in range(0,50):
        data={
            'url':pageurls[i].get('href'),
            'city':citys[i+1].text,
            'salary':salarys[i+1].text,
            'title':pageurls[i].get('title'),
            'company':companys[i].get('title'),
            'companyurl':companys[i].get('href'),
        }
        dataurl.insert_one(data)