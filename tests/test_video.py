def test_video(video1):
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_pl_video(video2):
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'


def test_broken_video(broken_video):
    assert broken_video.title is None
    assert broken_video.like_count is None
