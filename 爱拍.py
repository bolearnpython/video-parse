#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-12 12:23:10
# @Author  : bo (bo17096701774@gmail.com)
# @Link    : https://github.com/bolearnpython


import requests
from scrapy import Selector
# 爱拍
r = requests.get('http://www.aipai.com/c31/OT02JSAqJCRpJGsu.html')
sel = Selector(text=r.text, type='html')
url = sel.css('meta[property="og:videosrc"]::attr(content)').extract_first()
print(url)