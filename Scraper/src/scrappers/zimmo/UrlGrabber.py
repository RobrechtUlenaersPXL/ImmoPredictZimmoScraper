
from src.scrappers import WebDriver
from src.cleaner import Saver
from threading import Thread
from bs4 import BeautifulSoup
from os.path import exists
import csv


class UrlGrabber(Thread):

    base_url = "https://www.zimmo.be"

    def __init__(self, province: str):
        """
        Scrap the urls of all advertisement's webpage and return it to
        the Manager.

        :type province: str
        """

        Thread.__init__(self)
        print(f'[+] UrlGrabber: Start grabbing for {province}')

        self.source = f"https://www.zimmo.be/fr/province/{province}/a-vendre/?pagina=%s#gallery"
        #https://www.zimmo.be/fr/province/{province}/a-vendre/?sort=recent&sort_order=desc#gallery
        #"https://www.zimmo.be/fr/province/{province}/a-vendre/?pagina=%s#gallery"
        self.urls: list = []
        self.driver = WebDriver()

        # debug mode limits the amount of links that are pulled
        self.debug_mode = True
        self.province = province

    def get_urls(self):
        """Return a list of all urls of the given province."""

        # If the urls list is empty, start the grabber
        if not self.urls:
            self.run()

        # Then return the urls
        return self.urls

    def run(self):
        """Launch the threaded execution of this class."""
        self.__grab()
        self.driver.close()

    def __grab(self) -> None:
        """
        Grab the urls of the adverts from the source link.
        This method is called by run() and is threaded.
        """

        i = 0
        is_complete = False
        duplicates = 0

        while not is_complete:
            i += 1
            print(f"current page: {i}")

            # Fetch the page
        
            if (self.driver.get(self.source % i) is not None):
                self.soup = BeautifulSoup(self.driver.page_source(), "lxml")

                # Check if there are adverts or if debug limit is reached
                if (not self.soup.find('div', {"class": 'alert alert-danger'})) and (not self.debug_mode or (self.debug_mode and i <3) ) :

                    # Append all advertisement's links

                    
                    links = self.soup.find_all('a', {"class": 'property-item_link'}, href=True)
                    for link in links:
                        old_link = False
                        link = link.get("href")
                        # if link is not in csv append otherwise do not 

                        if exists(f'./data/{self.province}.csv'):
                            with open(f'./data/{self.province}.csv', newline='') as csvfile:
                                link_reader = csv.DictReader(csvfile)
                                for row in link_reader:
                                    if str(link) == row['url'][20:]:
                                        old_link = True
                                        duplicates +=1
                                    
                        # Append the link to the lis of links
                        if link and old_link == False:
                            self.urls.append(f"{UrlGrabber.base_url}{link}")

                # If the grabber reach the last page, stop the loop
                else:
                    is_complete = True
                    self.urls_saver()
                    print("found " + str(duplicates) + " duplicates ")

    @staticmethod
    def filter_house_apartment(string):
        """Filter and return the urls that are 'maison' or 'appartement'."""

        if "/maison/" in string or "/appartement/" in string:
            return string

        return None

    def urls_saver(self):
        Saver(self.urls,self.province).save()
