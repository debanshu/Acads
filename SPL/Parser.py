import re
import ParseTable
import sys
import Lexer

from ParseTable import *

def run(tokenStream):
    #print tokenStream
    Stack =[]
    #Stack.append("$")
    Stack.append("start")
    Input = tokenStream.split()
    #get first token
    t = Input[0]
    #Input.reverse()
    while Stack:
        top = Stack.pop()
        #check if non-terminal
        if top in pTable.keys(): 
            
            #get production rule
            p = pTable[top][t]
            #l = p.split()
            if p:
                for tk in reversed(p.split()):
                    if tk != "&epsilon":
                        Stack.append(tk)
            else:
                left=",".join(Input)
                return ("Syntax error at non terminal "+top+" with token "+t+" \nCouldn't parse the remaining tokens: "+left)
        else:
            if top == t:
                del Input[0]
                t = Input[0]
            else:
                left=",".join(Input)
                return ("Syntax error at terminal mismatch :"+top +" with token "+t +" \nCouldn't parse the remaining tokens: "+left)
                
    left=",".join(Input)
    if ( t == "$"):
        return( "Successfully parsed Code ")
    else:
        return("Successfully parsed code uptill token: "+t+" \nCouldn't parse the remaining tokens: "+left)    



if __name__ == '__main__':
    tokenStream = Lexer.run(sys.argv[1])
    print 'TokenStream'
    print '-----------'
    print tokenStream+" $"
    print(run(tokenStream+" $"))
  
