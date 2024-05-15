from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

# Requires solenium chromedriver installed
class ScraperDynamicPage:
    def __init__(self):
        self._url = None
        self._driver = None
        self._page_soup = None

    def open(self):
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        self._driver = webdriver.Chrome(options=driver_options)

    def close(self):
        self._driver.close()

    def load_page(self, url: str):
        allowed_url_prefixes = ("http://","https://")    
        if not url.lower().startswith(allowed_url_prefixes):
            url = "http://" + url;

        self._url = url
        try:
            self._driver.get(self._url)
        except WebDriverException:
            raise Exception("Failed to load page: {}".format(self._url))
            
        html = self._driver.page_source
        self._page_soup = BeautifulSoup(html, "html.parser")

    def find_robots_metatag_content(self):
        if self._page_soup == None:
            raise Exception("No page has been loaded.")
        
        # Split and flatan all the content values to return just one list of content values.
        result_robots_metatag_content_list = []
        for content_text in [robot_tag.get('content') for robot_tag in self._page_soup.find_all('meta', attrs={"name": "robots"})] :
            result_robots_metatag_content_list.extend(content_text.replace(" ","").split(','))

        return result_robots_metatag_content_list


        