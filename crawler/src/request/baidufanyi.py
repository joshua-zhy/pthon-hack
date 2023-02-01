import requests


def translate(kw):
    url = "https://fanyi.baidu.com/sug"

    #post 是 data get 是没有data的只有 params
    data = {
        "kw":kw
    }
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    
    resp = requests.post(url,data,headers).json()
    # print(resp['data'])
    
    for i in resp['data']:
        print("key:",i['k'],"trans:",i['v'],end='\n')
    

if __name__ == '__main__':
    
    translate(input("please input key word: "))
    
