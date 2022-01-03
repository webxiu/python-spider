# import urllib2
# import urllib.request


# response = urllib.request.urlopen("http://www.baidu.com/")
# html = response.read()
# print(html)


# ua_headers = {"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

# request = urllib.request.Request("http://www.baidu.com/", headers=ua_headers)
# response = urllib.request.urlopen(request)
# html = response.read()
# print(html)


from urllib import request,parse
url = "http://www.baidu.com/s"
ua_headers = {"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
keywords = input("请输入搜索关键字:")
ipt = {"wd": keywords}

wd = parse.urlencode(ipt) # 编码
fullurl = url + "?" + wd  # 拼接

req = request.Request(fullurl, headers=ua_headers)
response = request.urlopen(req)
html = response.read()
print(html)




print(wd)