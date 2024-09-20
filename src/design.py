

OUT_PARSE_OFFSET=1
REQ_PARSE_OFFSET=-1

delim=['+','-','/','*','**','(',')',',','[',']','sqrt','exp','expm1','ceil','floor','fmod','log1p','log10','sin','cos','tan','sinh','cosh','tanh']
prop_operators=['<','>','=','!']

class Design:

    def __init__(self,newdesign):
        #atributes
        self.design=None
        self.outs=[]
        self.ins=[]
        self.reqs=dict

        
        self.setDesign(newdesign)
        
        self.parseDesign(self.getDesign())

    def setDesign(self, newdesign :str):
        self.design = newdesign

    def getDesign(self):
        return self.design

    def parseDesign(self,design):
        self.outs=Design.extractOutputs(design)
        self.ins=Design.extractInputs(design,self.outs)
        
    @staticmethod
    def extractOutputs(design):
        designlist=design.split('|') #split between equations
        outs=[]
        for string in designlist:
            outs.append(string.split('=')[1].split()[0]) #split at = sign chose the second item then split at spaces to get output variable in the first item of the list
        return outs

    @staticmethod
    def extractInputs(design,outs): 
        designlist=design.split('|') #split between equations
        ins=[]
        for string in designlist:
            parsetemp=string.split(']')[0] #take only input equation
            for i in delim: #split it in variables
                parsetemp=parsetemp.replace(i,' ') 
            parsedstring=parsetemp.split()
            for j in parsedstring: # check if not an output
                if j in outs:
                    continue
                else:
                    ins.append(j) #store the input variables
        return ins


    @staticmethod
    def extractRequirements(design):
        reqs=dict()
        designlist=design.split('|') #split between equations
        for strings in designlist:
            requirements=strings.split("'")
            while '' in requirements: #remove empty strings
                requirements.remove('')
            requirements.pop(0)
            for string in requirements:
                #getting variable
                gotstuffbeforevar=False
                var=[]
                varstr=''
                foundvar=False
                for i in range(len(string)):# find the variable for this requirement and store it
                    if (string[i] not in prop_operators) and (string[i]!=' ') and (foundvar or not string[i].isdigit()):
                        foundvar=True
                        var.append(string[i])
                    else:
                        if foundvar:
                            varstr=''.join(var)
                            break
                        else:
                            continue
                
                #getting properties
                varpos=string.find(varstr)
                prop=[]
                lnum=[]
                lnumstr=''
                loper=[]
                loperstr=''

                numstr=''
                #before var
                for i in range(0,varpos,1): #find the numbers and the operators before the variables then store them in order in a list
                    if string[i].isdigit() or string[i]=='.':
                        lnum.append(string[i])
                    elif string[i] in prop_operators:
                        loper.append(string[i])
                if lnum:
                    lnumstr=''.join(lnum)
                    prop.append(lnumstr)
                else:
                    prop.append(None)
                if loper:
                    loperstr=''.join(loper)
                    prop.append(loperstr)
                else:
                    prop.append(None)
                
                #after var and get optimisations
                rnum=[]
                rnumstr=''
                roper=[]
                roperstr=''
                opt=[]
                optstr=''
                for i in range(varpos+len(var),len(string),1):# find the numbers and operators after variable and also find the optimisation parqameter
                    if string[i] in prop_operators:
                        roper.append(string[i])
                    elif string[i].isdigit() or string[i]=='.':
                        rnum.append(string[i])
                    elif string[i].isalpha() or string[i]=='_':
                                opt.append(string[i])
                                
               
                #store the info
                if roper:
                    roperstr=''.join(roper)
                    prop.append(roperstr)
                else:
                    prop.append(None)

                if rnum:
                    rnumstr=''.join(rnum)
                    prop.append(rnumstr)
                else:
                    prop.append(None)

                if opt:
                    optstr=''.join(opt)
                    prop.append(optstr)
                else:
                    prop.append(None)
                reqs[varstr]=prop #store them in a dictionary by variables

        return reqs
                
                
                    

    @staticmethod
    def testParsing():
        design="[ xylophone + y_1 ]   =  za_b  '20<xylophone<=30 max ''y_1 min'| [a*za_b]=w 'w=20''a=2'"
        print('Base design: '+design)
        outs=Design.extractOutputs(design)
        print("Outputs extracted: "+str(outs))
        ins=Design.extractInputs(design,outs)
        print("Inputs extracted: "+str(ins))
        reqs=Design.extractRequirements(design)
        print("Requirements extracted"+str(reqs))
        
