from urllib import request
import re  # 正则

# 爬虫类


class splider:
    def __init__(self):
        # 起始页
        self.page = 1
        # 爬取开关, 状态
        self.status = True

    def loadPage(self):
        idx = "index" if self.page == 1 else "index_" + str(self.page);
        url = "https://www.neihan8s.com/article/" + idx + ".html"
        # print("====", idx)
        # 设置headers模拟浏览器请求
        response = request.Request(url)
        res = request.urlopen(response)
        html = res.read().decode("utf-8")

        # 正则匹配标签内容
        reg = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
        lists = reg.findall(html)
        print(lists)
        self.writePage(lists)

    def writePage(self,lists):
        print("\n已写入"+str(self.page)+"页数据...\n")
        with open('duanzi.txt', 'a') as f:
            f.write('\n\n\n'.join(lists))
    # 循环爬取数据
    def startWork(self):
        while self.status:
            self.loadPage()
            enter = input("继续爬取数据请按[回车键], 退出请输入[Q]")
            if enter == "Q" or enter == "q":
                self.status = False
            self.page = self.page + 1

s = splider()
# s.loadPage()
s.startWork()
