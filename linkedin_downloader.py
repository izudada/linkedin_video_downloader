import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json


def lk_downloader():
    link = input("Enter the link to a LinkedIn post: \n")
    title = "_".join(link.split("-")[1:-3]) #   create title from post
    res = requests.get(link)    #   get post using request library
    #   send response to bs4
    soup = BeautifulSoup(res.text, features='html.parser')
    videos = soup.find_all('video') #   find video tag(s)
    #   extract video url
    result = json.loads(videos[0]['data-sources'])[0]['src']
    file_name = f"{title}.mp4"  #   create filename from title
    #   make request using video url
    video_url = requests.get(result, stream=True)

    #   stream video from response
    with open(file_name, 'wb') as f: 
        for chunk in video_url.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
        print(f"downloaded {file_name}")
    print("Downloded video sucessfully")

lk_downloader()
