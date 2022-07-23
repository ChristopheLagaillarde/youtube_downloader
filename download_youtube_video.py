# Program : download youtube video
# Description : This allow you to download a youtube video
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import pytube
from pytube import Stream


def download_youtube_video(link: str) -> None:

    youtube_video: pytube.__main__.YouTube = pytube.YouTube(link)
    download_video: Stream = youtube_video.streams.get_highest_resolution()
    download_video.download('videos\\')

    return None
