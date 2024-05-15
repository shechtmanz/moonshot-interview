from src.webscrape_legal_risk.risk_detector import RiskDetector, RiskResult
from src.helpers.llm_api.chat_gpt import ChatGpt

class TermsAndConditionRiskDetector (RiskDetector):
    _RISK_DESCRIPTION = "ChatGPT Terms & conditions interpretation"
    _TERM_OF_USE_LINK_TEXT = ("terms of use", "conditions of use", "terms of service")
    

    def __init__(self, url: str, llm: ChatGpt):
        super().__init__(url)
        self._llm = llm

    def evaluate_risk(self) -> RiskResult: 
        _legality_prompt = "Is scraping {} legal base on their terms and conditions. Summarize in one sentence".format(
            self.url.replace('https://', '').replace('http://','') )
        scrape_legality_response = self._llm.ask_chat(_legality_prompt)
        
        _legality_prompt_yes_no =  "Summarize it in one word, either yes or no"
        legality_response_yes_no = self._llm.ask_chat(_legality_prompt_yes_no)
        if (len(legality_response_yes_no.split()) != 1):
            raise Exception("Expected receive one world from the llm chat for the yes/no question: '{}', received: {}"
                            .format(_legality_prompt_yes_no, legality_response_yes_no))

        isScrapeLegal = self._convert_response_to_bool(legality_response_yes_no)
        
        if not isScrapeLegal:
            return RiskResult(TermsAndConditionRiskDetector._RISK_DESCRIPTION, scrape_legality_response)

    def _convert_response_to_bool(self, yes_no_answer: str) -> bool:
        return "yes" in yes_no_answer.lower()