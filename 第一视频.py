
import requests
from scrapy import Selector
# 第一视频
r = requests.get('http://www.v1.cn/video/14613697.shtml')
sel = Selector(text=r.text, type='html')
url = sel.css('param[name="FlashVars"]::attr(value)').re(r'videoUrl=(.*)')[0]
print(url)


