# Program : send notification
# Description : send a notification on windows10
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

from notifypy import Notify
from get_youtube_link_title import get_youtube_link_title
from download_youtube_video_thumbnail import download_youtube_video_thumbnail
from get_youtube_video_thumbnail_url import get_youtube_video_thumbnail_url


def send_notification(link_of_downloaded_video: str) -> None:
    video_title: str = get_youtube_link_title(link_of_downloaded_video)

    thumbnail_url: str = get_youtube_video_thumbnail_url(link_of_downloaded_video)
    download_youtube_video_thumbnail(thumbnail_url)

    notification: Notify = Notify()
    notification.title = video_title
    notification.message = 'The download is completed'
    notification.application_name = 'Youtube Downloader'
    notification.icon = 'thumbnail.jpg'
    notification.send()

    return None
