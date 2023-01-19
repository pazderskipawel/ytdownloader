from pytube import YouTube
from sys import argv

class Video:
    def __init__(self,link):
        self.link = YouTube(link)

    def info(self):
        link = self.link
        return link.title, link.author, link.views

    def download(self, action):
        link = self.link
        if (action==0):
            link.streams.get_audio_only().download()
        elif(action==1):
            link.streams.get_lowest_resolution().download()
        elif (action==2):
            link.streams.get_highest_resolution().download()