import numexpr
import math

class Rule:
    def __init__(self,newequation :str):
        self.setEquation(newequation)
        self.MakeVarDict()
        
        

        
    
    def setEquation(self,newequation :str):
        self.equation = newequation

    def getEquation(self):
        return self.equation

    
    def ExecuteRule66(self):
        
        return numexpr.evaluate(self.equation,local_dict=self.VarDict)

    def MakeVarDict(self):
        delim=['+','-','/','*','**','(',')',',']
        fcnlist=['sqrt','exp','expm1','ceil','floor','fmod','log1p','log10','sin','cos','tan','sinh','cosh','tanh']
        vrs=self.equation
        
        for i in delim:
            vrs=vrs.replace(i,' ')

        
        vrs=vrs.split()
        

        cnt=0
        for i in range(len(vrs)):
            if vrs[i-cnt].isdigit() or (vrs[i-cnt] in fcnlist):
                vrs.pop(i-cnt)
                cnt=cnt+1



        self.VarDict=dict()
        for i in vrs:
            self.VarDict[i]= "notBinded"
        

    def setVarDict(self,Varname,value):
        self.VarDict[Varname]=value
    
    def getVarDict(self):
        return self.VarDict

   


