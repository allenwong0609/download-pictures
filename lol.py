import requests
import re
import json


def getHeroesImages():
    # 获取英雄序号的js源代码
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    html_js = requests.get(url_js).text

    req = '"keys":(.*?),"data"'
    list_js = re.findall(req, html_js)
    dic_js = json.loads(list_js[0])
    # print(dic_js)

    # 拼接图片url   http://ossweb-img.qq.com/images/lol/web201310/skin/big266000.jpg
    pic_url = []
    for hero_id in dic_js:
        for i in range(15):
            if i < 10:
                pic_id = '00' + str(i)
            else:
                pic_id = '0' + str(i)
            url_id = hero_id + pic_id
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + url_id + '.jpg'
            pic_url.append(url)
    # print(all_url)

    # 获取下载路径
    files_path = []
    path = 'E:\Python\自制笔记\爬取英雄资料\\files\\'
    for hero_name in dic_js.values():
        # print(hero_name)
        for i in range(15):
            path1 = path + hero_name + str(i) + ".jpg"
            files_path.append(path1)
    # print(files_path)

    # 下载图片
    index = 0
    for pic in pic_url:
        res = requests.get(pic)
        index += 1
        if res.status_code == 200:
            print("正在下载:%s" % files_path[index])
            with open(files_path[index], "wb") as f:
                f.write(res.content)

getHeroesImages()
