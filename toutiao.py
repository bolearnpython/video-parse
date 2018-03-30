import base64
import binascii
import random
import re

import requests


def right_shift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n
r = requests.get('http://www.toutiao.com/a6296462662335201793/')
vid = re.findall(r"videoid\s*:\s*'([^']+)',\n", r.text)[0]
r = str(random.random())[2:]
n = '/video/urls/v/1/toutiao/mp4/%s' % vid + '?r=' + r
c = binascii.crc32(n.encode())
s = right_shift(c, 0)
url = "http://i.snssdk.com/video/urls/v/1/toutiao/mp4/{}?r={}&s={}".format(
    vid, r, s)
r = requests.get(url).json()['data']
main_url = r['video_list']['video_1']['main_url']
video_url = base64.standard_b64decode(main_url)
print(video_url)
