import requests,os
from lxml import html

# 导入etree 
# from lxml import html
# etree = html.etree
 
domain = 'https://www.umei.cc/meinvtupian/siwameinv/'

resp = requests.get(url = domain)
resp.encoding = 'utf-8'
# print(resp.text) 

etree = html.etree

html = etree.HTML(resp.text) 

divs = html.xpath('//*[@id="infinite_scroll"]') 

# print(divs)

urls = []
titles = []


for div in divs:
    urls = div.xpath('.//img/@data-original')
    titles = div.xpath('.//img/@alt')    



data = dict(zip(titles,urls))
# print(data)

for title,url in data.items():
    # print(key,value)
    resp = requests.get(url)
    print(title+".jpg") 
    with open(f"../../data/sex_girl_pic/2/{title}.jpg",mode="wb")as f:
        f.write(resp.content)
    resp.close()   
