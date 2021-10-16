# ImmoPredictZimmoScraper
Scraper used in our immopredict it project, expanded upon https://github.com/Joffreybvn/bot-scrape-zimmo

## setup
just use 01_build_image and 02_run_container to build and run docker container for the scraper

## using scraper
python3 main.py -p X

X is the number of the province you want to scrape with the following array being the provinces ordered 0 - 10:  

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
              "region-de-bruxe lles-capitale"  
          ]

## DEBUG MODE
Scraper/src/scrappers/zimmo/UrlGrabber.py  
has the following code on line 30, it limits the scaper to 42 entries, just put it on false to turn it off:  

        #debug mode limits the amount of links that are pulled  
        self.debug_mode = True  
        
## Captchas
currently there is no good workaround for captchas, paste the captcha link in another brower, solver the captcha and past the new zimmo url in the selenium chrome browser.
