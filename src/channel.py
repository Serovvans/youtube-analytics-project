import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        youtube = self.get_service()
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()["items"][0]
        self.title = channel["snippet"]["title"]
        self.description = channel["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = int(channel["statistics"]["subscriberCount"])
        self.video_count = int(channel["statistics"]["videoCount"])
        self.view_count = int(channel["statistics"]["viewCount"])

    def get_info(self) -> dict:
        """Возвращает информацию о канале"""
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = self.get_info()
        print(json.dumps(info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        # Создаем объект работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def to_json(self, file_name: str) -> None:
        """Сохраняет данные о канале в json файл"""
        file = os.path.join("..", "data", file_name)
        info = {"title": self.title, "description": self.description, "url": self.url,
                "subscriber_count": self.subscriber_count,
                "view_count": self.view_count, "video_count": self.video_count}

        with open(file, "w") as f:
            json.dump(info, f)

    @property
    def channel_id(self):
        return self.__channel_id

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count
