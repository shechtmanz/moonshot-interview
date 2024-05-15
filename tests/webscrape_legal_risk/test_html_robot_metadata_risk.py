import pytest
from unittest import mock
from src.webscrape_browser.scraper_dynamic_page import ScraperDynamicPage
from src.webscrape_legal_risk.html_robots_metadata_risk_detector import HtmlRobotsMetadaRiskDetector

@pytest.mark.parametrize("robot_content_list_mock, preventative_robot_content_list_expected", [
    (['noindex'], ['noindex']),
    (['noindex','dummy_content'], ['noindex']),
    (['Noindex'], ['noindex']) ])
@mock.patch('src.webscrape_legal_risk.html_robots_metadata_risk_detector.ScraperDynamicPage')
def test_metada_risk_found(scraper_mock, robot_content_list_mock, preventative_robot_content_list_expected):
    scraper_mock.find_robots_metatag_content.return_value = robot_content_list_mock
    
    url = 'www.dummy.com'
    robot_metada_risk = HtmlRobotsMetadaRiskDetector (url, scraper_mock)
    risk_result = robot_metada_risk.evaluate_risk()
    assert risk_result.description == "HTML robot metadata risk"
    assert risk_result.result_message == \
        "The website specified the following tags in the HTML header metadata: {}".format(preventative_robot_content_list_expected)
    

@pytest.mark.parametrize("robot_content_list_mock", [['dummy_content'], []])
@mock.patch('src.webscrape_legal_risk.html_robots_metadata_risk_detector.ScraperDynamicPage')
def test_metada_risk_no_risk(scraper_mock, robot_content_list_mock):
    scraper_mock.find_robots_metatag_content.return_value = robot_content_list_mock
    
    url = 'www.dummy.com'
    robot_metada_risk = HtmlRobotsMetadaRiskDetector (url, scraper_mock)
    risk_result = robot_metada_risk.evaluate_risk()

    assert not risk_result 
    