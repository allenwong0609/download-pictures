import requests
import os


def getHeroesImages():
    # 访问目标网站
    url = 'http://lol.qq.com/act/a20180725hextech/awrads.html'
    html = requests.get(url)
    # print(res)

    # 获取图片url http://ossweb-img.qq.com/images/lol/appskin/37005.jpg
    sona_url = []
    for i in range(10):
        sona = 'http://ossweb-img.qq.com/images/lol/appskin/3700' + str(i) + '.jpg'
        sona_url.append(sona)
    # print(sona_url)

    # 获取下载路径
    files_path = []
    path = 'E:\Python\自制笔记\爬取英雄资料\sona\\'
    for n in range(10):
        path1 = path + 'sona' + str(n) + '.jpg'
        files_path.append(path1)

    # 下载图片
    if not os.path.exists('sona'):
        os.mkdir('sona')
    index = 0
    for i in sona_url:
        res1 = requests.get(i)
        index += 1
        if res1.status_code == 200:
            print('正在下载...')
            with open(files_path[index], 'wb') as f:
                f.write(res1.content)

getHeroesImages()