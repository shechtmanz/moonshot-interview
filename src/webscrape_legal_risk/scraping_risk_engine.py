from src.webscrape_legal_risk.html_robots_metadata_risk_detector import HtmlRobotsMetadaRiskDetector 
from src.webscrape_legal_risk.tc_risk_detector import TermsAndConditionRiskDetector
from src.helpers.webscrape_browser.scraper_dynamic_page import ScraperDynamicPage
from src.webscrape_legal_risk.risk_detector import RiskDetector, RiskResult
from src.helpers.llm_api.chat_gpt import ChatGpt

class ScrapingRiskEngine:

    def __init__(self, url: str):
        self._scraper = ScraperDynamicPage()
        self._llm = ChatGpt()
        self._risk_detectors = (
            HtmlRobotsMetadaRiskDetector(url, self._scraper),  
            TermsAndConditionRiskDetector(url, self._llm), 
        )

    def evaluate_risk(self) -> list[RiskResult]: 
        risks_detected: RiskResult = []

        # scrape the page
        try:
            self._scraper.open()
        
            # evaluate the risks
            risk_detector: RiskDetector
            for risk_detector in self._risk_detectors:
                identified_risk = risk_detector.evaluate_risk()
                if identified_risk:
                    risks_detected.append(identified_risk)
        finally:
            self._scraper.close()

        return risks_detected

        # deal with errors
