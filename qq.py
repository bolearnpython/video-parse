import datetime
import hashlib
import json
import random
import re
import time
import requests


def createGUID():
    str_16 = 'abcdef0123456789'
    return ''.join(random.choice(str_16) for i in range(32))

vid = 'z00244ovjdf'
tm = str(int(time.time()))
flowid = createGUID()
guid = createGUID()
now_day = datetime.datetime.now()
now_weekday = now_day.weekday()
enver = '7.' + str(now_weekday + 1)
magic = ["06fc1464", "4244ce1b", "77de31c5",
         "e0149fa2", "60394ced", "2da639f0", "c2f0cf9f"][now_weekday]
ckey = magic + vid + tm + "*#06#" + '10201'
md5 = hashlib.md5()
md5.update(ckey.encode())
ckey = md5.hexdigest()


url = "https://vd.l.qq.com/proxyhttp"
param = 'charge=0&defaultfmt=auto&otype=json&guid={guid}&flowid={flowid}_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.41&host=film.qq.com&refer=http%3A%2F%2Ffilm.qq.com%2Ffilm_index_prevue%2Findex.html%3FfirstVid%3Dz00244ovjdf&ehost=http%3A%2F%2Ffilm.qq.com%2Ffilm_index_prevue%2Findex.html&sphttps=1&tm={tm}&spwm=4&vid={vid}&defn=mp4&fhdswitch=0&show1080p=0&isHLS=1&dtype=3&defsrc=1&encryptVer={enver}&cKey={ckey}'.format(
    guid=guid, vid=vid, tm=tm, flowid=flowid, enver=enver, ckey=ckey)
payload = "{\"adparam\":\"\",\"buid\":\"vinfoad\",\"vinfoparam\":\"%s\"}" % param
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'origin': "https://jx.maoyun.tv",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    'content-type': "text/plain",
    'dnt': "1",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,ko;q=0.8",
    'cache-control': "no-cache",
    'postman-token': "5982daa0-eec9-a327-be8c-f3d0580b2c57"
}
response = requests.request("POST", url, data=payload, headers=headers)
data = re.search(r'{.*}', response.json()['vinfo']).group()
urls_list = json.loads(data)['vl']['vi'][0]['ul']['ui']
urls = [i['url'] + i['hls']['pt']for i in urls_list]
print(urls)
