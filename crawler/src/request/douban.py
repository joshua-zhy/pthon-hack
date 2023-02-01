import requests

def crawl_douban():
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    
    params = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }
    resp = requests.get(url=url,params=params,headers=headers)
    moive_list = resp.json()
    
    for movie in moive_list:
        for k,v in movie.items():
            print(k,v) 
            
    
    
    resp.close() #关闭连接
if __name__ == '__main__':
    crawl_douban()
    