# Revixa1 2023
import rules
import argparse
import random




def main():

    parser = argparse.ArgumentParser(prog='Thumb Rule Designer')
  
    # Adding Argument
    parser.add_argument('inputRule',
                    metavar ='EQN',
                    type = str,
                    help ='enter a python equation')

    args = parser.parse_args()
    print(args)

    
 
    simpleRule = rules.Rule(args.inputRule)
    print(simpleRule.getEquation())
    print(simpleRule.getVarDict())
    for i in simpleRule.getVarDict():
        simpleRule.setVarDict(i,random.randint(0,100))
    print(simpleRule.getVarDict())
    print(simpleRule.ExecuteRule66())
    






if __name__ == "__main__":
    main()
