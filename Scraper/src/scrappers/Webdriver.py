
import time
from random import choice
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


# driver = "/Users/noahalvarezgonzalez/Drivers/chromedriver"  # Noah
driver = "/usr/lib/chromium-browser/chromedriver"  # Joffrey


PROXIES = [
    "176.31.141.21:51327",
    "51.77.163.186:8080",
    "91.121.33.63:1000",
    "176.31.141.20:51327",
    "54.38.110.35:48034",
    "51.254.182.54:1000",
    "159.8.114.37:80",
    "151.80.201.162:1080",
    "51.68.61.17:5000"
]


class WebDriver:

    def __init__(self, use_proxy=True, fast_method=True, delay=2):

        self.delay = delay

        # Load the options
        self.options = self.__create_options(fast_method)
        #self.captcha_options = self.__create_options(False)
        self.__activate_proxy(use_proxy)

        # Initialize the driver
        
        #self.driver = webdriver.Chrome(driver, chrome_options=self.options)
        self.driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=self.options)
        #self.captcha_driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=self.captcha_options)
        self.driver.implicitly_wait(86400)  # Max waiting time: 24h

    def get(self, url):
        if url:
            self.driver.get(url)

            # Wait for the page to load
            try:
                self.driver.find_element_by_xpath("//*[@data-ga='Feedback,click,Side button']")
            except TypeError:
                print[f"[x] Failed to load the page. Maybe the website is blocking us ? - {url}"]
                pass
            else:
                return True

        return None

    def page_source(self):
        return self.driver.page_source

    def close(self):
        self.driver.close()

    @staticmethod
    def __create_options(fast_method):
        options = webdriver.ChromeOptions()

        if fast_method:

            # Block the ads
            options.add_extension("./src/scrappers/extensions/ublock_origin_1_29_2_0.crx")

            # Use a small windows
            options.add_argument("window-size=1,1")

            # Block the images and the javascript
            preferences = {
                "profile.managed_default_content_settings.javascript": 2,
                "profile.managed_default_content_settings.images": 2
            }
            options.add_experimental_option("prefs", preferences)

        return options

    def __activate_proxy(self, use_proxy):

        if use_proxy:

            # Initialize the proxy
            proxy = Proxy()
            proxy.proxyType = ProxyType.MANUAL
            proxy.autodetect = False

            # Load a random proxy
            self.proxy = choice(PROXIES)
            proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = self.proxy

            # Apply it to self.options
            self.options.Proxy = proxy
            self.options.add_argument("ignore-certificate-errors")
