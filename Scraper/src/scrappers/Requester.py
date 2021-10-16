
import requests


# https://www.xml-sitemaps.com/
class Requester:

    options = {
        'Accept': '*/*',
        'Host': 'www.zimmo.be',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9) Gecko/2008051206 Firefox/3.0',
    }

    def __init__(self):
        pass

    @staticmethod
    def get(url):
        return requests.get(url, headers=Requester.options)
