import requests,re,csv

def tiantang_movie():
    domain = "https://www.dytt89.com"

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    # 1.发送请求
    resp = requests.get(url=domain, headers=headers, verify=False)  # 去掉安全验证

    resp.encoding = 'gb2312'

    # print(resp.text)

    # 2.解析
    obj1 = re.compile(r'2023必看热片.*?<ul>(?P<pages>.*?)</ul>', re.S)

    pages = obj1.search(resp.text)

    # print(pages.group("pages"))

    obj2 = re.compile(r"<a href='(?P<sub_page_url>.*?)'", re.S)

    sub_page_urls = obj2.finditer(pages.group("pages"))

    # 3.子页面的url
    sub_url_list = []

    for i in sub_page_urls:
        # print(i.group("sub_page_url"))
        sub_url = domain + i.group("sub_page_url")
        # print(sub_url)
        sub_url_list.append(sub_url)

    # print(sub_page_urls)
    # 4.请求子页面的数据
    get_sub_url(sub_url_list)


def get_sub_url(sub_url_list):

    obj3 = re.compile(r'◎片　　名(?P<movie_name>.*?)<br />.*?'
                    r'◎简　　介<br />(?P<desc>.*?)<br />.*?'
                    r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)">',re.S)   

        #3.写入
    with open("../../data/taintang_movie.csv",mode="a") as f:
        csvWrite = csv.writer(f) #创建 csv 格式的 write
        for i in sub_url_list:
        # print(i)
            headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

            # 1.发送请求
            resp = requests.get(url=i, headers=headers, verify=False)  # 去掉安全验证

            resp.encoding = 'gb2312'

            # print(resp.text)
            movie_names = obj3.finditer(resp.text)
            # print(movie_names.group("movie_name").strip())
            # print(movie_names.group("desc").strip())
            # print(movie_names.group("download_url").strip())
    
   
   
        
            for i in movie_names:
                dict = i.groupdict()#name year rating_num  desc 全是他的key  v是数据 
                csvWrite.writerow(dict.values())
    
   


        



if __name__ == '__main__':
    tiantang_movie()
