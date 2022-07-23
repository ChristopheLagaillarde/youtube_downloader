# Program : get youtube video thumbnail url
# Description : get the url of the thumbnail of the video
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import pytube


def get_youtube_video_thumbnail_url(link: str) -> str:
    youtube_video: pytube.__main__.YouTube = pytube.YouTube(link)

    return youtube_video.thumbnail_url

