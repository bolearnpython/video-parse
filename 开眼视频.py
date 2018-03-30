import re
import requests

url = 'http://www.eyepetizer.net/detail.html?vid=18376'
vid = re.search('vid=(\d+)', url).group(1)
api_url = 'http://baobab.kaiyanapp.com/api/v1/video/%s' % vid
r = requests.get(api_url)
for info in r.json()['playInfo']:
    print(info['name'], ': ', info['url'])
