from urllib import request, parse


def loadpage(fullurl, filename):
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    req = request.Request(fullurl, headers=ua_headers)
    html = request.urlopen(req).read()
    return html

def writepage(html, filename):

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(html.decode(encoding="utf-8"))
    print("结束")

def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage+1):
        pn = (page-1) * 50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "&pn=" + str(pn)
        print("=======",fullurl)
        # 发起请求
        html = loadpage(fullurl, filename)
        # 保存
        writepage(html, filename)


kw = input("请输入爬取的贴吧名称:")
beginPage = int(input("请输入起始页:"))
endPage = int(input("请输入结束页:"))

url = "https://tieba.baidu.com/f?"
key = parse.urlencode({"kw": kw})
fullurl = url + key
tiebaSpider(fullurl, beginPage, endPage)
