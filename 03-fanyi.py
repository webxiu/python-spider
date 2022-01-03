from urllib import request, parse
import json

# url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
txt = input("请输入要翻译的内容:")

formData = {
    "i": txt,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15699357603457",
    "sign": "e4d8588dd1e22516d791ecf779125139",
    "ts": "1569935760345",
    "bv": "c4e95e621267f4d4577f554f2869b772",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlM"
}


data = parse.urlencode(formData).encode("utf-8")
response = request.Request(url,data=data)
result = request.urlopen(response).read().decode("utf-8")

dec = json.loads(result) # 转为字典
fan = dec['translateResult'][0][0]['tgt']

print(type(dec))
print(fan) # 翻译结果