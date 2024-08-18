# import requests
# from bs4 import BeautifulSoup

# header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" }

# base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="


N = int(input())
aa = set([])

for i in range(N):
    i = input()
    aa.add(i)

bb = list(aa)
cc = sorted(bb, key=len)
cc.sort()

for i in cc:
    print(i)
    