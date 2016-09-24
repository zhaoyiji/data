import raw_data


def test_fetch():
    remote = raw_data.RawData()
    url = raw_data.RealData.make_url()
    data = remote.fetch(url)
    for item in data:
        print item

    assert 0
