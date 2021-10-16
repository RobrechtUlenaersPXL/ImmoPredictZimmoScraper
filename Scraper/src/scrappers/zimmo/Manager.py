
import concurrent
from concurrent.futures import wait
from concurrent.futures import ThreadPoolExecutor

from src.scrappers.zimmo.UrlGrabber import UrlGrabber
from src.scrappers.zimmo.Scrapper import Scrapper
from src.scrappers import WebDriver


class Manager:

    
        
    

    def __init__(self,province_index):

        """
        The Manager class coordinate the UrlGrabber and the Scrapper:

        It retrieve the URLs given by an UrlGrabber, then instantiate multiple
        threaded Scrappers and return their result to the Cleaner.
        """
        # Provinces to scrap numbered 0 to 10
   
        self.provinces = [
            "anvers",
            "brabant-flamand",
            "brabant-wallon",
            "flandre-occidentale",
            "flandre-orientale",
            "hainaut",
            "liege",
            "limbourg",
            "luxembourg",
            "namur",
            "region-de-bruxelles-capitale"
        ]
        self.province = []
        self.province.append(self.provinces[province_index])
        self.urls = []

    def grabber(self, workers): 
        """Retrieve the urls of all selling advertisement from zimmo.be."""
        #
        for url in self.__thread_call(self.__url_grabber,self.province , workers):
            self.urls += url.result()

    @staticmethod
    def __url_grabber(province):
        return UrlGrabber(province).get_urls()

    @staticmethod
    def scrapper(urls):
        scrapper = Scrapper(urls)
        scrapper.start()
        scrapper.join()

        return scrapper.get_data()

        # https://stackoverflow.com/questions/15143837/how-to-multi-thread-an-operation-within-a-loop-in-python
    @staticmethod
    def __thread_call(func, sources, max_workers):
        """
        Call a given function ('func') multiple time simultaneously.

        :param func: The function to start multiple simultaneous instances.
        :param sources: The list of provinces
        :param max_workers: the maximum instances to start at once.

        :return: An iterator with the content returned by the 'func' instances.
        """

        # Start simultaneously multiple instances of the given function
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(func, entry) for entry in sources]

            # Return an iterator of lists
            return concurrent.futures.as_completed(futures)
