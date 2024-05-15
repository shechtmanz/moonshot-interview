import pytest
from src.helpers.webscrape_browser.scraper_dynamic_page import ScraperDynamicPage

# www.shopbop.com is a static website, it returns the full HTML
# by testing http on Shopbop we test redirction to https.
@pytest.fixture(params=["https://www.shopbop.com", "http://www.shopbop.com"])
def shopbop_scraper(request):
    url = request.param
    scraper = ScraperDynamicPage()
    scraper.open()
    scraper.load_page(url)
    yield scraper
    scraper.close()

# www.etsy.com is a dynamic website, it returns renders on the client with JS
@pytest.fixture
def etsy_scraper():
    url = "https://www.etsy.com"
    scraper = ScraperDynamicPage()
    scraper.open()
    scraper.load_page(url)
    yield scraper
    scraper.close()

# Warning: this test might break if shopbop.com changes their <metadata name="ROBOTS" Content="index, follow"> tag - consider mocking
def test_find_robots_meta_static_site(shopbop_scraper):
    robots_tag_content_strings_list = shopbop_scraper.find_robots_metatag_content()
    assert 'index' in robots_tag_content_strings_list
    assert 'follow' in robots_tag_content_strings_list

# Warning: this test might break if etsy.com adds a metadata tag to their HTML header - consider mocking
def test_find_robots_meta_dynamic_site(etsy_scraper):
    robots_tag_content_strings_list = etsy_scraper.find_robots_metatag_content()
    assert not robots_tag_content_strings_list
    