import requests
r=requests.get("http://google.com")#hanbit으로바꿔보기.
r.raise_for_status()
#print(r.status_code)
#print(r.text)
with open("data.html","w",encoding="UTF-8") as f:
    f.write(r.text)
