
from src.scrappers.zimmo import Manager
from src.cleaner import Cleaner, Merger

from itertools import zip_longest
import concurrent
from concurrent.futures import wait
from concurrent.futures import ThreadPoolExecutor


class Collector:

    def __init__(self, grabber_workers=1, scrapper_workers=1, url_pool_size=10):
        """
        Collect the raw data from the Manager and save it into CSV
        files through the Cleaner.
        """
        self.url_pool_size = url_pool_size
        self.grabber_workers = grabber_workers
        self.scrapper_workers = scrapper_workers

    def start(self,province_index):

        # Grab the urls to scrap
        manager = Manager(province_index)
        manager.grabber(10)

        # Print starting message
        total_urls_number = len(manager.urls)
        print(f"[+] Scrapping phase started: 0/{total_urls_number}.")

        scrapped_urls = 0

        # Group the urls 10 by 10
        grouped_total_urls = self.grouper(manager.urls, self.url_pool_size)

        with ThreadPoolExecutor(max_workers=self.scrapper_workers) as executor:
            futures = [executor.submit(Manager.scrapper, urls) for urls in grouped_total_urls]

            for entry in concurrent.futures.as_completed(futures):

                # Iterate the scrapped_urls and print a status message
                scrapped_urls += self.url_pool_size
                print(f"[i] Urls scrapped: {scrapped_urls}/{total_urls_number}.")
                
                Cleaner(entry.result(),manager.province).clean()

        print(f"[i] Urls scrapped: {total_urls_number}/{total_urls_number} - Complete !")

        # Merge the pickles
        Merger().merge(manager.province)

    @staticmethod
    def grouper(iterable, n, fill_value=None):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fill_value)
