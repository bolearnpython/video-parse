import re

import requests
cna_url = 'http://log.mmstat.com/eg.js'
r = requests.get(cna_url)
cna = re.search(r'Etag="(.*?)"', r.text).group(1)
vid = 'XMjkwNjExNzg5Ng=='
url = 'https://ups.youku.com/ups/get.json?vid={vid}&ccode=03020101&client_ip=192.168.1.1&client_ts=1522307821&utid={cna}'.format(
    vid=vid, cna=cna)
headers = {'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.8,ko;q=0.6',
           'dnt': '1',
           'origin': 'https://m.youku.com',
           'referer': 'https://m.youku.com/video/id_XMjkzODkxMTM0NA==.html?spm=a2hww.20023042.m_223465.5~5~5~5!2~5!3~5~A&source=',
           'user-agent': 'HwVPlayer;2.21.307;Android;7.0;BLN-AL10' }
r = requests.get(url, headers=headers)
video_url = r.json()['data']['stream'][0]['m3u8_url']
print(video_url)


#失效了 又是客户端201