from src.channel import  Channel
class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id=video_id    # id видео
        self.title_video = self.print_info_video()["items"][0]["snippet"]["title"]     # название видео
        self.url = self.print_info_video()["items"][0]["snippet"]["thumbnails"]["default"]["url"]   # ссылка на видео
        self.views_count = self.print_info_video()["items"][0]["statistics"]["viewCount"] # количество просмотров
        self.like_count = self.print_info_video()["items"][0]["statistics"]["likeCount"] # количество лайков
    def __str__(self):
        return self.title_video
    def print_info_video(self) -> None:

         """Выводит в консоль информацию о видео в формате словаря."""
         youtube = Channel.get_service()
         video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
         return video_response
class PLVideo(Video ):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video )
        self.id_video=id_video
        self.id_playlist=id_playlist
a=Video('AWX4JnAnjBE')
print(a.print_info_video()  )
