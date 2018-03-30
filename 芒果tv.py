
import json
import os
import random
import re

import requests

vid = re.search(
    r'/(\d+).html', 'http://www.mgtv.com/b/292031/3789569.html').group(1)
r = requests.get('http://pcweb.api.mgtv.com/player/video?&video_id=%s' % vid)
data = json.loads(r.text)
streams = data['data']['stream']
stream_domains = data['data']['stream_domain']
for stream in streams:
    print(stream['name'])
    stream_domain = random.choice(stream_domains)
    url = stream_domain + stream['url']
    r = requests.get(url)
    data = json.loads(r.text)
    m3u8_url = data['info']
    print(m3u8_url)
