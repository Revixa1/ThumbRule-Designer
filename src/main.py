# Revixa1 2023
import rules
import argparse
import random
from icecream import ic




def main():

    parser = argparse.ArgumentParser(prog='Thumb Rule Designer')
  
    # Adding Argument
    parser.add_argument('inputRule',
                    metavar ='EQN',
                    type = str,
                    help ='enter a python equation')

    args = parser.parse_args()
    ic(args)

    
 
    simpleRule = rules.Rule(args.inputRule)
    ic(simpleRule.getEquation())
    ic(simpleRule.getVarDict())
    for i in simpleRule.getVarDict():
        simpleRule.setVarDict(i,random.randint(0,100))
    ic(simpleRule.getVarDict())
    ic(simpleRule.ExecuteRule66())
    

def ParseInput(optimisationDesign):





if __name__ == "__main__":
    main()
