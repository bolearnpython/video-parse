import base64
import requests
from scrapy import Selector


def decode(encoded_string):
    def getHex(param1):
        return {
            'str': param1[4:],
            'hex': ''.join(list(param1[:4])[::-1]),
        }

    def getDec(param1):
        loc2 = str(int(param1, 16))
        return {
            'pre': list(loc2[:2]),
            'tail': list(loc2[2:]),
        }

    def substr(param1, param2):
        loc3 = param1[0: int(param2[0])]
        loc4 = param1[int(param2[0]): int(param2[0]) + int(param2[1])]
        return loc3 + param1[int(param2[0]):].replace(loc4, "")

    def getPos(param1, param2):
        param2[0] = len(param1) - int(param2[0]) - int(param2[1])
        return param2

    dict2 = getHex(encoded_string)
    dict3 = getDec(dict2['hex'])
    str4 = substr(dict2['str'], dict3['pre'])
    return base64.b64decode(substr(str4, getPos(str4, dict3['tail'])))

r = requests.get('http://www.meipai.com/media/596371059')
sel = Selector(text=r.text, type="html")
secure_url = sel.css(
    'head > meta[property="og:video:secure_url"]::attr(content)').extract_first()
video_url = decode(secure_url)
print(video_url)
