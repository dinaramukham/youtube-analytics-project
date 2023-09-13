#import json
import os
from googleapiclient.discovery import build
#import isodate

from helper.youtube_api_manual import printj


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id=channel_id

    def print_info(self ) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.environ['API__KEY']
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id , part='snippet,statistics').execute()
        print(printj(channel))

obzbzbz=Channel('UC-OVMPlMA3-YCIeg4z5z23A')
obzbzbz.print_info()