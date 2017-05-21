# 大乐透

import requests

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Cookie':'d_c0="AEDCaKnAHQuPThY8qI5w9pblKFsZDkIqK8A=|1483755223"; _zap=21ff4117-b795-4c45-a6b0-5ab18366a64e; q_c1=aaa177d5401e49ce88a6d1909d3d3880|1489290889000|1483755222000; r_cap_id="NTk2MjMzZWQ2MjA2NGM1YWI5NDQ4YWM5M2YwM2I0Y2Y=|1489290932|eb6e7cab851fa9243d049c901bd0bd56f781e948"; cap_id="NGJmNmRkNDViYjU1NGI5ZmFkNDUxMGM4MzAyY2I4OTA=|1489290932|c943af653facb0b8e57467d89d4bc53f1936c2ba"; l_cap_id="ZTI2Njk5ODdlMjljNDY5MmIyYmQ2YjQyOGUxMTkwYWY=|1489290932|7d13d016b783b707fe7cc81447f006e04dceb051"; nweb_qa=heifetz; _xsrf=18a9ed88176da255ec8c80d2d4b78376; aliyungf_tc=AQAAAC80OlzOQgcARHB6ffg985I4uurk; __utmt=1; __utma=51854390.1776040400.1488717600.1489321512.1490247352.9; __utmb=51854390.15.9.1490247412670; __utmc=51854390; __utmz=51854390.1490247352.9.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20150715=1^3=entry_date=20150715=1; z_c0=Mi4wQUJDTWtsNXVaQWdBUU1Kb3FjQWRDeGNBQUFCaEFsVk43MVBzV0FBOFlpbkRoVVdmNVhkMUFydE1aMTdobTdNR2x3|1490247414|a47b6f744ee208f1d285170cf83018594f66ee5a',

}

def lottery_dlt(term):
    # 利用_term获取历史数据
    # url='http://www.lottery.gov.cn/api/lottery_kj_detail_new.jspx?_ltype=4&_term=17055'
    url = 'http://www.lottery.gov.cn/api/lottery_kj_detail_new.jspx?_ltype=4&_term={}'.format(term)

    web=requests.get(url,headers=headers)

    json=web.json()
    print(json[0]['lottery']['number'])