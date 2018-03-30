import re
import requests
import json
import random

m = re.search(r'/show/([\w~-]+)\.htm',
              'http://www.miaopai.com/show/Qo3uI72UKWF-EriUFLL~VA__.htm')
vid = m.group(1)
r = requests.get('http://gslb.miaopai.com/stream/%s.json?token=' % vid)
data = json.loads(r.text)
urls = [r['scheme'] + r['host'] + r['path'] for r in data['result']]
print(urls)