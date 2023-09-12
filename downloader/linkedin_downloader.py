import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json


def _lk_downloader(link, path):
    """
        A function that take a url of a linkedIn post
        and dowload a video attached to it if exists
    """
    title = "_".join(link.split("-")[1:-3]) #   create title from post
    try:
        res = requests.get(link)    #   get post using request library
    except Exception as e:
        print(e)
        return "Please connect to the internet before downloading video"
    #   send response to bs4

    soup = BeautifulSoup(res.text, features='html.parser')
    videos = soup.find_all("video") #   find video tag(s)

    #   check if linkedin post has a video
    if len(videos) == 0:
        return "Invalid LinkedIn url. No video was found"
    
    #   extract video url
    result = json.loads(videos[0]['data-sources'])[0]['src']
    file_name = f"{title}linkedin_video.mp4"  #   create filename from title

    #   make request using video url
    try:
        video_url = requests.get(result, stream=True)
    except Exception as e:
        print(e)
        return "Please connect to the internet before downloading video"
    #   stream video from response
    with open(path+file_name, 'wb') as f: 
        for chunk in video_url.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
        print(f"downloaded {file_name}")
    return file_name
