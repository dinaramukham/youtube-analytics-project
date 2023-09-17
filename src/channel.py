
import os
from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title=self.print_info()["items"][0]["snippet"]["title"]
        self.description=self.print_info()["items"][0]["snippet"]["description"]
        self.url=self.print_info()["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count=self.print_info()["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.print_info()["items"][0]["statistics"]["videoCount"]
        self.viewCount= self.print_info()["items"][0]["statistics"]["viewCount"]
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в формате словаря."""
        youtube = Channel.get_service()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, name_new_file):
        with open(name_new_file, 'w') as f:
            f.write(f"channel_id : {self.channel_id},\n"  # 
                    f"title : {self.title},\n "
                    f"description : {self.description},\n "
                    f"url : {self.url}, \n"
                    f"subscriber_count : {self.subscriber_count},\n "
                    f"video_count : {self.video_count},\n "
                    f"viewCount : {self.viewCount}. ")
    @classmethod
    def get_service(cls):
        """ создать специальный объект для работы с API """
        api_key: str = os.getenv('API__KEY')
        return  build('youtube', 'v3', developerKey=api_key)
