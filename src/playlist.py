import datetime

from src.youtube import YouTubeApi


class PlayList(YouTubeApi):
    """Класс для представления плейлиста на youtube"""

    def __init__(self, pl_id: str):
        """Инициализация нового объекта. Получает название и создаёт url с помощью id"""
        self.__pl_id = pl_id

        youtube = self.get_service()
        playlist = youtube.playlists().list(id=pl_id, part='snippet').execute()
        self.title = playlist["items"][0]["snippet"]["title"]

        self.url = f"https://www.youtube.com/playlist?list={pl_id}"

    def get_videos(self) -> list[str]:
        """Возвращает список id видео"""
        youtube = self.get_service()

        videos = [item["contentDetails"]["videoId"] for item in
                  youtube.playlistItems().list(part="contentDetails",
                                               playlistId=self.__pl_id).execute()["items"]]

        return videos

    @staticmethod
    def get_time(str_time: str) -> dict[str]:
        """Перевод строки длительности видео в словарь с элементами времени"""
        str_time = str_time[2:]
        time = dict()
        last = 0
        if "H" in str_time:
            time["H"] = int(str_time[last:str_time.find("H")])
            last = str_time.find("H") + 1
        if "M" in str_time:
            time["M"] = int(str_time[last:str_time.find("M")])
            last = str_time.find("M") + 1
        if "S" in str_time:
            time["S"] = int(str_time[last:str_time.find("S")])

        return time

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает суммарную длительность видео в плейлисте"""
        videos = self.get_videos()
        youtube = self.get_service()

        sm = datetime.timedelta()
        for item in videos:
            duration = youtube.videos().list(id=item,
                                             part="contentDetails").execute()["items"][0]["contentDetails"]["duration"]
            time = self.get_time(duration)

            sm += datetime.timedelta(hours=time.get("H", 0),
                                     minutes=time.get("M", 0),
                                     seconds=time.get("S", 0))
        return sm

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        videos = self.get_videos()
        youtube = self.get_service()

        best_video = max(videos, key=lambda x: youtube.videos().list(id=x,
                                                                     part="statistics").execute()["items"][0][
            "statistics"]["likeCount"]
                         )
        return f"https://youtu.be/{best_video}"


if __name__ == "__main__":
    pl = PlayList("PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw")
    print(pl.show_best_video())
