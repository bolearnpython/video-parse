import json
import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36', }
m = re.search(r'/(\w+).html',
              'http://c.m.163.com/news/a/C42K63S1000181N1.html')
doc_id = m.groups()[0]
api_url = 'http://c.m.163.com/nc/article/%s/full.html' % doc_id
r = requests.get(api_url, headers=headers)
data = json.loads(r.text)
videos = data[doc_id]['video']
for video in videos:
    print(video.get('mp4Hd_url'))
    print(video.get('mp4_url'))
