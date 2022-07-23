# Program : download youtube video thumbnail
# Description : This script will download the youtube video thumbnail
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

import requests


def download_youtube_video_thumbnail(link_to_thumbnail: str) -> None:

    img_data = requests.get(link_to_thumbnail).content
    with open('thumbnail.jpg', 'wb') as handler:
        handler.write(img_data)

    return None
