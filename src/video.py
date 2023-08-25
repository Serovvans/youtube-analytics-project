from src.youtube import YouTubeApi


class Video(YouTubeApi):
    """Класс для youtube-видео"""
    def __init__(self, video_id: str):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id

        youtube = self.get_service()
        video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                      id=video_id).execute()
        try:
            self.title: str = video['items'][0]['snippet']['title']
            self.view_count: int = video['items'][0]['statistics']['viewCount']
            self.like_count: int = video['items'][0]['statistics']['likeCount']
            self.url: str = f"https://youtu.be/{video_id}"
        except IndexError:
            self.title = self.view_count = self.like_count = self.url = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс для связи видео с 1 плейлистом"""
    def __init__(self, video_id: str, pl_id: str):
        super().__init__(video_id)
        self.pl_id = pl_id
