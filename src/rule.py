import numexpr

class Rule():



    def __Init__(self,newequation: str):
        
        self.setEquation(newequation)
        

        
    
    def setEquation(newequation: str):
        self.equation: str= newequation

    def getEquation():
        return self.equation


    





    
    def ExecuteRule66():
        return numexpr.evaluate(self.getEquation)



