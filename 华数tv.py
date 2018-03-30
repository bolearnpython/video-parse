import re
import requests
import base64
import hashlib
import xmltodict


def url_decode(param1):
    # md5_hex是用来计算md5哈希值的
    param2 = md5_hex('wasu!@#48217#$@#1')
    loc7 = md5_hex(param2[0:16])
    loc8 = md5_hex(param2[16:32])
    loc11 = loc7 + md5_hex(loc7 + param1[0:4])
    loc12 = len(loc11)
    param1 = base64.b64decode(param1[4:])
    loc13 = len(param1)

    loc14 = []
    loc15 = []
    loc16 = 0
    while loc16 < 128:
        loc14.append(loc16)
        loc15.append(ord(loc11[loc16 % loc12]) & 255)
        loc16 += 1

    loc16 = 0
    loc17 = 0
    loc19 = 0
    while loc16 < 128:
        loc17 = (loc17 + loc14[loc16] + loc15[loc16]) % 128
        loc19 = loc14[loc16]
        loc14[loc16] = loc14[loc17]
        loc14[loc17] = loc19
        loc16 += 1

    loc17 = 0
    loc16 = 0
    loc18 = 0
    loc20 = []
    while loc16 < loc13:
        loc18 = (loc18 + 1) % 128
        loc17 = (loc17 + loc14[loc18]) % 128
        loc19 = loc14[loc18]
        loc14[loc18] = loc14[loc17]
        loc14[loc17] = loc19
        t = param1[loc16] & 255 ^ loc14[(loc14[loc18] + loc14[loc17]) % 128]
        loc20.append(chr(param1[loc16] & 255 ^ loc14[
                     (loc14[loc18] + loc14[loc17]) % 128]))
        loc16 += 1

    return (''.join(loc20))[26:]


def md5_hex(data):
    m = hashlib.md5()
    m.update(data.encode())
    return m.hexdigest()

url = 'https://www.wasu.cn/Play/show/id/9474892'
# get vid
vid = re.search('/id/(\d+)', url).group(1)
# get key
r = requests.get(url)
key = re.search('_playKey\s*=\s*\'(\w+)\'', r.text).group(1)

r = requests.get(
    'http://www.wasu.cn/Api/getPlayInfoById/id/%s/datatype/xml' % vid)
d = xmltodict.parse(r.text)
for k, v in d['root']['mp4'].items():
    r = requests.get(
        'http://apiontime.wasu.cn/Auth/getVideoUrl?id=%s&key=%s&url=%s' % (vid, key, v))
    encoded_url = xmltodict.parse(r.text)['root']['video']
    print(k, url_decode(encoded_url))
