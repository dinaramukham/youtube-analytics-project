from src.channel import  Channel
#from helper.youtube_api_manual import  printj
class Video:
    def __init__(self, video_id: str) -> None:
        try:
            self.video_id=video_id    # id видео
            self.title = self.print_info_video()["items"][0]["snippet"]["title"]     # название видео
            self.url = self.print_info_video()["items"][0]["snippet"]["thumbnails"]["default"]["url"]   # ссылка на видео
            self.views_count = self.print_info_video()["items"][0]["statistics"]["viewCount"] # количество просмотров
            self.like_count = self.print_info_video()["items"][0]["statistics"]["likeCount"] # количество лайков
        except IndexError:
            self.video_id = video_id  # id видео
            self.title = None
            self.url = None
            self.views_count = None
            self.like_count = None

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
#a=Video('X4JnAnjBE') # AWX4JnAnjBE
#print(a.title_video     )


