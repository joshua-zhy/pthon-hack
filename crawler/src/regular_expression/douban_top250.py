import requests,re,csv

def douban_movie_top250(url):
    # 1.请求
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    
    resp = requests.get(url=url,headers=headers).text
    
    #2.re 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?'
                     r'<span class="inq">(?P<desc>.*?)</span>',re.S) #re.S 让 . 匹配换行
    # .*? 非贪婪模式 可以匹配换行和空白字符
    # ?P<content>  后面的 .*?会被放到content里面
    results = obj.finditer(resp) #返回的是迭代器 需要 group() 得到 
    
    
    #3.写入
    with open("../../data/douban_top.csv",mode="a") as f:
        csvWrite = csv.writer(f) #创建 csv 格式的 write
    
        for i in results:
            dict = i.groupdict()#name year rating_num  desc 全是他的key  v是数据 
            # print(i.group("name"))
            # print(i.group("year").strip())
            # print(i.group("rating_num"))
            # print(i.group("desc"))
            dict['year'] = dict['year'].strip()

            csvWrite.writerow(dict.values())



if __name__ == '__main__':

    for i in range(0,251,25):
        url = f"https://movie.douban.com/top250?start={i}"
        douban_movie_top250(url)
    

    
    