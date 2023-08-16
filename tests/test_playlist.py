def test_get_videos(playlist):
    assert playlist.get_videos() == ['feg3DYywNys', 'MtWXwMCAApY', 'nApYYXYL9qA', 'cUGyMzWQcGM']


def test_get_time(playlist):
    assert playlist.get_time("РТ8H") == {"H": 8}
    assert playlist.get_time("РТ23M9S") == {"M": 23, "S": 9}


def test_total_duration(playlist):
    assert str(playlist.total_duration) == "1:49:52"


def test_attrs(playlist):
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_show_best_video(playlist):
    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
