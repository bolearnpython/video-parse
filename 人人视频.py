# 人人视频
# http://rr.tv/#/video/172278
import requests
video_id = 172278
headers = {
    'clientVersion': '0.1.0',
    'clientType': 'web',
}
api_url = 'http://api.rr.tv/v3plus/video/getVideoPlayLinkByVideoId'
r = requests.post(api_url, data={'videoId': video_id}, headers=headers)
print(r.json()['data']['playLink'])
