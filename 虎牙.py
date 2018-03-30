#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-12 12:20:55
# @Author  : bo (bo17096701774@gmail.com)
# @Link    : https://github.com/bolearnpython


# 虎牙
import json
import random
import re

import requests
from scrapy import Selector

vid = re.search(r'/play/(.*).html', 'http://ahuya.duowan.com/play/14743000.html').group(1)
play_api = 'http://v-api-play.huya.com/index.php?partner=vhuya&r=vhuyaplay%2Fvideo&vid={vid}'.format(vid=vid)
r = requests.get(play_api)
data = json.loads(r.text)
for item in data['result']['items']:
    definition = item['definition']
    urls = item['transcode']['urls']
    print(definition)
    print(random.choice(urls))
