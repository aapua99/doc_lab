import urllib.request as rq


class UrlFileReader:
    def __init__(self, timeout=5):
        pass

    def read_file_from_url(self, file_url):
        return rq.urlopen(url = file_url, timeout = 5).read().decode('utf-8').split()
