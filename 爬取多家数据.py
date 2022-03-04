import requests
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}


def baidu(company):
    url = 'https://www.baidu.com/s?rtt=4&tn=news&word=' + company
    res = requests.get(headers=headers, url=url)
    res.encoding = 'utf-8'
    res = res.text
    # 对数据进行清洗和提取
    # 提取网址和来源
    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    # 提取日期和来源
    p_date = '<span class="c-color-gray2 c-font-normal" aria-label=".*">(.*?)</span>'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray c-font-normal c-gap-right" aria-label=".*">(.*?)</span>'
    source = re.findall(p_source, res)
    # 数据清洗
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        print(str(i+1)+'.'+title[i]+'('+source[i]+' '+date[i]+')')
        print(href[i])
    # --------------------------------------
    # 保存进文件
    file1 = open('E:\\数据挖掘报告.txt', 'a')
    file1.write(company+'数据挖掘完毕！'+'\n'+'\n')
    for i in range(len(title)):
        file1.write(str(i+1)+'.'+title[i]+'('+source[i]+' '+date[i]+')'+'\n')
        file1.write(href[i]+'\n')
        file1.write('----------------------------'+'\n'+'\n')


companies = ['华能信托', '阿里巴巴', '京东', '百度集团']
for i in companies:
    baidu(i)
    print(i+"百度新闻爬取成功")
