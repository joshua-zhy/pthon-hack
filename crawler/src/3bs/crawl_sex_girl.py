# bs 

# find("标签名",attrs={"属性":"值"}) #没有属性可以不写
# find_all("标签名",attrs={"属性":"值"})

# .text 拿到文本
# get("href") 拿属性
# https://www.umei.cc/meinvtupian/xingganmeinv/297445.htm
# https://www.umei.cc/meinvtupian/xingganmeinv/297445_2.htm
import requests,os

from bs4 import BeautifulSoup

def crawl_sex_girl():
    filePath = "/home/joshua/Desktop/python/crawler/data/sex_girl_pic/"
    main_url = 'https://www.umei.cc/meinvtupian/xingganmeinv/'
    resp = requests.get(main_url)
    resp.encoding = 'utf-8'
    # print(resp.text)
    main_page = BeautifulSoup(resp.text,"html.parser")#网页源代码 使用 html.parser解析
    div_list = main_page.find_all("div",attrs={"class":"item_b clearfix"})
    # print(div_list)
    for div in div_list:
        a_list = div.find("a")
        page_title = a_list.text
        
        #创建文件夹
        folderPath = filePath + page_title
        mkdir(folderPath) 
        
        page_url = main_url +a_list.get("href").split("/")[-1]
        get_first_img( folderPath , page_url)
        get_second_img( folderPath , page_url)
        get_third_img(  folderPath , page_url)
 

     
def mkdir(path):
     
    folder = os.path.exists(path)
     
    if not folder:                
    	os.makedirs(path)         

 
            
def get_first_img(page_title, page_url):
    resp = requests.get(page_url)
    resp.encoding = 'utf-8'    
    # print(resp.text)
    main_page = BeautifulSoup(resp.text,"html.parser")#网页源代码 使用 html.parser解析
    div_pics = main_page.find_all("div",attrs={"class":"big-pic"})  
    
    with open(f"{page_title}/1.jpg",mode="wb") as f:
        for div in div_pics:
            img_src = div.find("img").get("src")
            print(img_src)    
            resp = requests.get(img_src)
            f.write(resp.content)
            resp.close()
            
    
    
def get_second_img(page_title, page_url):   
    # https://www.umei.cc/meinvtupian/xingganmeinv/297445.htm
    # https://www.umei.cc/meinvtupian/xingganmeinv/297445_2.htm
    
    str = page_url.split("/")[-1].split(".")[0]
    # print(str)
    replace_str = str.split(".")[0]+"_2" 
    
    # print(replace_str)
    page_url= page_url.replace(str,replace_str)
    # print(page_url)
    resp = requests.get(page_url)
    resp.encoding = 'utf-8'    
    main_page = BeautifulSoup(resp.text,"html.parser")#网页源代码 使用 html.parser解析
    div_pics = main_page.find_all("div",attrs={"class":"big-pic"})  
    
    with open(f"{page_title}/2.jpg",mode="wb") as f:
        for div in div_pics:
            img_src = div.find("img").get("src")
            print(img_src)    
            resp = requests.get(img_src)
            f.write(resp.content)
            resp.close()

def get_third_img(page_title, page_url):   
    # https://www.umei.cc/meinvtupian/xingganmeinv/297445.htm
    # https://www.umei.cc/meinvtupian/xingganmeinv/297445_2.htm
    
    str = page_url.split("/")[-1].split(".")[0]
    # print(str)
    replace_str = str.split(".")[0]+"_2" 
    
    # print(replace_str)
    page_url= page_url.replace(str,replace_str)
    # print(page_url)
    resp = requests.get(page_url)
    resp.encoding = 'utf-8'    
    main_page = BeautifulSoup(resp.text,"html.parser")#网页源代码 使用 html.parser解析
    div_pics = main_page.find_all("div",attrs={"class":"big-pic"})  
    
    with open(f"{page_title}/3.jpg",mode="wb") as f:
     for div in div_pics:
            img_src = div.find("img").get("src")
            print(img_src)    
            resp = requests.get(img_src)
            f.write(resp.content)
            resp.close()       
    
if __name__ == '__main__':
    crawl_sex_girl()