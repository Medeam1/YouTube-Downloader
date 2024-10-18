from logging import fatal

import requests
from pytube import YouTube

API_KEY = ''
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'



def video_search(keyword):
    params = {
        "part": "id,snippet",
        "key": API_KEY,
        "q": keyword,
        "maxResults": 5,
        "type": "video",
    }

    r = requests.get(BASE_URL, params=params)
    result = []
    for number, data in enumerate(r.json()["items"]):
        video_title = data["snippet"]["title"]
        video_id = data["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        result.append(f'{number + 1}: {video_title} --> {video_url}')
    return "\n".join(result)

keyword = input("Въведете дума за търсене: ")
print(video_search(keyword))




