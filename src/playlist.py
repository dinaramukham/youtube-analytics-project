from src.channel import Channel
from src.video import Video
from datetime import timedelta

import isodate


class PlayList:
    def __init__(self, id_pl):
        self.id_pl = id_pl
        self.title = self.print_info_playlist()['items'][0]['snippet']['title']
        self.url = self.print_info_playlist()['items'][0]['snippet']['thumbnails']['default']['url']

    def print_info_playlist(self):
        youtube = Channel.get_service()
        playlists = youtube.playlists().list(id=self.id_pl,
                                             part='snippet',
                                             maxResults=50,
                                             ).execute()
        return playlists

    def id_video_playList(self):
        """получить все id видеороликов из плейлиста в виде списка"""
        youtube = Channel.get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=self.id_pl,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    @property
    def total_duration(self):
        youtube = Channel.get_service()
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.id_video_playList())
                                               ).execute()
        list_time_delta = []
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            list_time_delta.append(duration)
        sum_delta_time = timedelta(hours=0, minutes=0, seconds=0)
        for index in range(0, len(list_time_delta)):
            sum_delta_time += list_time_delta[index]

        return sum_delta_time

    def show_best_video(self):
        video_ids = self.id_video_playList()
        max_show = 0
        url=None
        for video_id in video_ids:
            exam = Video(video_id)
            if max_show < int(exam.like_count):
                max_show = int(exam.like_count)
                url = exam.url
        return url


