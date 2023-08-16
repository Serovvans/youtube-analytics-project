import pytest

from src.channel import Channel
from src.video import Video, PLVideo
from src.playlist import PlayList


@pytest.fixture(scope="session")
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture(scope="session")
def highload():
    return Channel('UCwHL6WHUarjGfUM_586me8w')


@pytest.fixture(scope="session")
def video1():
    return Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб


@pytest.fixture(scope="session")
def video2():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


@pytest.fixture(scope="session")
def playlist():
    return PlayList("PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw")
