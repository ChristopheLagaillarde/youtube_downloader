# Program : youtube downloader
# Description : This program allow you to download youtube video
# Date : 23/07/22
# Author : Christophe Lagaillarde
# Version : 1.0

from sys import argv
from send_notification import send_notification
from download_youtube_video import download_youtube_video


def main() -> None:
    link: str = argv[1]

    download_youtube_video(link)
    send_notification(link)

    return None


if __name__ == '__main__':
    main()
