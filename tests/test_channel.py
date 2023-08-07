def test_get_info(channel):
    assert channel.get_info()["items"][0]["snippet"]["title"] == "MoscowPython"


def test_attributes(channel):
    assert channel.title == "MoscowPython"
    assert channel.url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
    assert channel.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"


def test_str(channel):
    assert str(channel) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


def test_add(channel, highload):
    assert channel + highload > 100100


def test_sub(channel, highload):
    assert channel - highload < -48300
    assert highload - channel == -1*(channel - highload)


def test_comparison(channel, highload):
    assert (channel > highload) is False
    assert (channel >= highload) is False
    assert (channel < highload) is True
    assert (channel <= highload) is True
    assert (channel == highload) is False
