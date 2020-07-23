import json
import urllib.request


class out:
    link: str
    title: str
    description: str


def get_all_video_in_channel(channel_id):
    api_key = "api key"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)
    video_des = []
    video_title = []
    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(i['id']['videoId'])
                video_title.append(i['snippet']['title'])
                video_des.append(i['snippet']['description'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_title, video_links, video_des
