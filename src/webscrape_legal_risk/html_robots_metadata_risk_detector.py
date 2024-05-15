from src.webscrape_legal_risk.risk_detector import RiskDetector, RiskResult
from src.webscrape_browser.scraper_dynamic_page import ScraperDynamicPage

class HtmlRobotsMetadaRiskDetector (RiskDetector):
    
    _RISK_DESCRIPTION = "HTML robot metadata risk"
    _SCRAPING_PREVENTIVE_ROBOT_CONTENT_TOKENS = ['noindex', 'nofollow']

    def __init__(self, url: str, scraper: ScraperDynamicPage):
        super().__init__(url)
        self._scraper = scraper

    def evaluate_risk(self) -> RiskResult: 
        self._scraper.load_page(self.url)
        
        # Look for the ROBOTS metadata in the HTML header.
        robots_tag_content_strings_list = [contentVal.lower() for contentVal in self._scraper.find_robots_metatag_content()]
            
        # check whether the robots metadata content contains at least one of the preventive tokens (intersection of the two lists)
        metadata_tags = list(
                set(HtmlRobotsMetadaRiskDetector._SCRAPING_PREVENTIVE_ROBOT_CONTENT_TOKENS) & 
                set(robots_tag_content_strings_list))
       
        if metadata_tags:
            risk_message = "The website specified the following tags in the HTML header metadata: {}".format(metadata_tags)
            return RiskResult(HtmlRobotsMetadaRiskDetector._RISK_DESCRIPTION, risk_message)

        
