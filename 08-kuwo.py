#!/usr/bin/env python3 
# encoding:utf-8
# 自动创建文件夹
import os
import requests 
from urllib.request import urlopen
from tqdm import tqdm

# 伪造浏览器身份信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn', 
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1641199840; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1641199840; _ga=GA1.2.998670654.1641199840; _gid=GA1.2.1725738576.1641199840; kw_token=RIJF5B0M3W; _gat=1',
    'csrf': 'RIJF5B0M3W',
}

#下载header
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1641199840; _ga=GA1.2.998670654.1641199840; _gid=GA1.2.1725738576.1641199840; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1641211125',
}

#创建目录
if not os.path.exists('./music'):
    os.mkdir('./music')

searchSong = input('请输入你想要搜索的歌曲/歌手:')
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=559bd950-6c85-11ec-b7b0-2f67cecc5334'.format(searchSong)


res = requests.get(url, headers=headers).json()
print(res)



def download_from_url (url, dst):
    # 获取文件长度
    try:
        file_size = int(urlopen(url).info().get('Content-Length', -1))
    except Exception as e:
        print(e)
        print("错误，访问url: %s 异常" % url)
        return False
    # 文件大小
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size 
    
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])

    # 访问url进行下载
    req = requests.get(url, headers=header, stream=True)
    try:
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
    except Exception as e:
        print(e)
        return False

    pbar.close()
    return True

for musicData in res['data']['list']: 
    musicName = musicData['name']
    musicRid = musicData['rid']

    with open('./music/' + musicName + '.mp3', 'wb') as f:
        musicApi = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=57a19031-6c8c-11ec-b7b0-2f67cecc5334'.format(str(musicRid))
        # print('地址:',musicApi)
        musicInfo = requests.get(musicApi, headers=headers).json()
        # print(musicInfo) 
        if musicInfo['code']==200:
            durl = musicInfo['data']['url']
            # 获取二进制文件
            print('\n\n正在下载: {}...\n'.format(musicName),durl) 
            # 获取音乐文件二进制 content
            musicContent = requests.get(durl, headers=headers2).content
            f.write(musicContent)
            print('\n下载成功!') 
        else:
            print('\n\n====歌曲:' + musicName + '\t为付费歌曲不能下载\n\n') 


print('\n\n\n===========下载完成===========') 