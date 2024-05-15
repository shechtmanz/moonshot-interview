import pytest
from unittest import mock
from src.webscrape_legal_risk.tc_risk_detector import TermsAndConditionRiskDetector

@mock.patch('src.webscrape_legal_risk.tc_risk_detector.ChatGpt')
def test_tc_evaluate_risk(chat_gpt_mock):
    long_gpt_response = "long response from chat GPT, stating that it is pobably not legal"
    chat_gpt_mock.ask_chat.side_effect = [long_gpt_response,"No."]

    tc_detector = TermsAndConditionRiskDetector("http://www.dummy.com", chat_gpt_mock)
    risk_results = tc_detector.evaluate_risk()
    
    assert risk_results.description == "ChatGPT Terms & conditions interpretation"
    assert risk_results.result_message == long_gpt_response


@mock.patch('src.webscrape_legal_risk.tc_risk_detector.ChatGpt')
def test_tc_evaluate_risk_no_risk_found(chat_gpt_mock):
    long_gpt_response = "long response from chat GPT, stating that it is legal to scraoe"
    chat_gpt_mock.ask_chat.side_effect = [long_gpt_response,"Yes."]

    tc_detector = TermsAndConditionRiskDetector("http://www.dummy.com", chat_gpt_mock)
    risk_results = tc_detector.evaluate_risk()
    
    assert not risk_results

@mock.patch('src.webscrape_legal_risk.tc_risk_detector.ChatGpt')
def test_tc_evaluate_risk_unexpected_yes_no_response(chat_gpt_mock):
    with pytest.raises(Exception):
        long_gpt_response = "long response from chat GPT, stating that it is legal to scraoe"
        chat_gpt_mock.ask_chat.side_effect = [long_gpt_response,"Yes 2words"]

        tc_detector = TermsAndConditionRiskDetector("http://www.dummy.com", chat_gpt_mock)
        risk_results = tc_detector.evaluate_risk()