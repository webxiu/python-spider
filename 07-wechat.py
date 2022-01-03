import itchat
import jieba
# from wordcloud import WordCloud

# 获取微信好友签名 (微信禁止了网页登录)

itchat.login()
friends = itchat.get_friends()
tlist = []
for i in friends:
    # print(i['NickName'], i['Signature'])
    req = i['Signature'].replace("span", "").replace("class", "")
    tlist.append(req)

text = "".join(tlist)
print(text)

wordList = jieba.cut(text, cut_all=True) # 分割词
spaceList = " ".join(wordList            # 连接词
# 生成词云
myword = WordCloud(background_color="white", max_font_size=40, font_path="ygyxsziti2.0.ttf")

words.to_file("a.png")

