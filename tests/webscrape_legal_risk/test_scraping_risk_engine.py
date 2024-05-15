import pytest
from unittest import mock
from src.webscrape_browser.scraper_dynamic_page import ScraperDynamicPage
from src.webscrape_legal_risk.risk_detector import RiskDetector
from src.webscrape_legal_risk.scraping_risk_engine import ScrapingRiskEngine, RiskResult


class DummyRiskDetector (RiskDetector):
    def __init__(self, url: str, risk_description, risk_message, identified_risk = True):
        super().__init__(url)
        self._risk_description = risk_description
        self._risk_message = risk_message
        self._identified_risk = identified_risk
    
    def evaluate_risk(self) -> RiskResult: 
        if self._identified_risk == False:
            return None
        
        return RiskResult(self._risk_description, self._risk_message)

def test_metada_risk_found_risk(mocker):
    risk_detector_engine = ScrapingRiskEngine("www.dummy.com")
    mocker.patch.object(risk_detector_engine, '_risk_detectors', [DummyRiskDetector("www.dummy.com", "Dummy risk description", "dummy risk message")])
    risk_result_list = risk_detector_engine.evaluate_risk()

    assert risk_result_list == [RiskResult("Dummy risk description", "dummy risk message")]

def test_metada_risk_found_multiple_risks(mocker):
    risk_detector_engine = ScrapingRiskEngine("http://www.dummy.com")
    mocker.patch.object(risk_detector_engine, '_risk_detectors', [DummyRiskDetector("www.dummy.com", "Dummy risk description1", "dummy risk message1"), \
                                                                  DummyRiskDetector("www.dummy.com", "Dummy risk description2", "dummy risk message2")])
    risk_result_list = risk_detector_engine.evaluate_risk()

    assert risk_result_list == [RiskResult("Dummy risk description1", "dummy risk message1"), \
                                         RiskResult("Dummy risk description2", "dummy risk message2")]
    

def test_metada_risk_no_risk_found(mocker):
    risk_detector_engine = ScrapingRiskEngine("http://www.dummy.com")
    mocker.patch.object(risk_detector_engine, '_risk_detectors', [DummyRiskDetector("www.dummy.com", None, None, identified_risk = False)])
    risk_result_list = risk_detector_engine.evaluate_risk()

    assert risk_result_list == []

def test_metada_risk_one_of_two_risk_found(mocker):
    risk_detector_engine = ScrapingRiskEngine("http://www.dummy.com")
    mocker.patch.object(risk_detector_engine, '_risk_detectors', [DummyRiskDetector("www.dummy.com", None, None, identified_risk = False), \
                                                                  DummyRiskDetector("www.dummy.com", "Dummy risk description2", "dummy risk message2")])
    risk_result_list = risk_detector_engine.evaluate_risk()

    assert risk_result_list == [RiskResult("Dummy risk description2", "dummy risk message2")]