import os

from googleapiclient.discovery import build


class YouTubeApi:
    """Реализует общий метод доступа к сервисам youtube для всех api объектов"""
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        # Создаем объект работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube
