import Calc
import sympy
from process_latex import process_sympy




class Rule():



    def __Init__(self,newequation: str):
        self.Calc=Calc()
        self.setEquation(newequation)
        self.setRuleElements(self.getEquation())
        
  #  def setState(newstate: int):
  #      self.state: int=newstate
    
    def setEquation(newequation: str):
        self.equation: str=process_sympy(newequation)

    def getEquation():
        return self.equation: str

    #def setConstants(newdictionaryConstants):
    #    self.dictionaryConstants=newdictionaryConstants

   # def setInputVariables(newdictionaryVariables):
   #     self.dictionaryVariables=newdictionaryVariables

    def setRuleElements(newequation: str):
       # self.RuleElements=newequation.split('+','-','*','/','**',)



    def getRuleElements():
       # self.RuleElements=dict(self.dictionaryConstants)
       # self.RuleElements.update(dictionaryVariables)
        return self.RuleElements

    
    def ExecuteRule66():
        sympify(self.getEquation).evalf()



