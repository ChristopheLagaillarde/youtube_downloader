# Program : get youtube link's title
# Description : This allow you to get a youtube video's title using it's link
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import pytube


def get_youtube_link_title(link: str) -> str:
    youtube_video: pytube.__main__.YouTube = pytube.YouTube(link)

    return youtube_video.title
