from src.webscrape_legal_risk.scraping_risk_engine import ScrapingRiskEngine
from src.webscrape_legal_risk.risk_detector import RiskResult

from src.helpers.llm_api.chat_gpt import ChatGpt

def print_result(risk_result_list: list[RiskResult]):
    print ()

    if not risk_result_list:
        print ("No risk to scrape this website were identified.")
    else:
        print ("The following risks to scrape the website were identified:")
        for risk in risk_result_list:
            print ("--> {}".format(risk))


def main():
    url = input("Input the website page you would like to check the scraping risk for [default: https://www.etsy.com]:") 
    if not url:
        url = "https://www.etsy.com"
    
    risk_engine = ScrapingRiskEngine(url)
    risk_result_list = risk_engine.evaluate_risk()
    
    print_result(risk_result_list)

if __name__ == '__main__':
    main()