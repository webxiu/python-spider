from urllib import request
import json

enter = input("请输入搜索类别:") #热门  美剧  英剧  韩剧  日剧  国产剧  港剧  日本动画  综艺  纪录片

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
# url = "https://movie.douban.com/j/search_subjects?type=movie&tag="+enter+"A8&page_limit=50&page_start=0"

response = request.Request(url)
result = request.urlopen(response).read().decode("utf-8")

dec = json.loads(result) #转成字典

print(dec['subjects']) # 获取单项