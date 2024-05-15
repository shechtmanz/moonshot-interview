from abc import ABC, abstractmethod

class RiskResult:
    def __init__(self, description: str, result_message: str):
        self.description = description
        self.result_message =  result_message

    def __eq__(self, other): 
            if not isinstance(other, RiskResult):
                return NotImplemented

            return self.description == other.description and \
                self.result_message == other.result_message
    def __repr__(self) -> str:
         return "Risk description: {} ; Risk message: {}".format(self.description, self.result_message)

class RiskDetector(ABC):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def evaluate_risk(self) -> RiskResult: 
        pass
