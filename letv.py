import time

import requests

def calcTimeKey(t):
    ror = lambda val, r_bits, : (
        (val & (2**32 - 1)) >> r_bits % 32) | (val << (32 - (r_bits % 32)) & (2**32 - 1))
    magic = 185025305
    return ror(t, magic % 17) ^ magic
vid = 31392179
url = 'http://player-pc.le.com/mms/out/video/playJson?id={}&platid=1&splatid=101&format=1&tkey={}&domain=www.le.com&region=cn&source=1000&accesyx=1'.format(
    vid, calcTimeKey(int(time.time())))
r = requests.get(url)
info = r.json()['msgs']
url_part1 = 'http://play.g3proxy.lecloud.com'
url_part3 = '&termid=1&m3v=1&format=1&expect=3&hwtype=un&ostype=Windows10&p1=1&p2=10&vid={vid}&sign=letv'.format(
    vid=vid)
dispatch = info["playurl"]["dispatch"]
urls = [(url_part1 + dispatch[i][0] + url_part3, i) for i in dispatch]
print(urls)
