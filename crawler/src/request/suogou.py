import requests
search = input("input search keywords: ")

url =f'https://www.sogou.com/web?query={search}'
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}



resp = requests.get(url,headers).text
print(resp)

