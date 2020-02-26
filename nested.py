#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Sasha Lukas w/ help Chris"

import sys

if sys.version_info[0] < 3:
    raise Exception("Need Python 3")

def main(args):
    """Add your code here"""
    if len(sys.argv) != 2:
        print 'Please add a filename as a second argument'
        sys.exit(1)
    filename = sys.argv[1]
    print(filename)
    fileToOpen = open(filename)
    fileToWrite = open("output.txt", "a")
    

    # charDict = { --Karen
    #     "parasts": ["(*", "*)"],
    #     "parens": ["(", ")"],
    #     "squares": ["[", "]"],
    #     "curlies": ["{", "}"],
    #     "alligators": ["<", ">"]
    # }
    charDict={">":"<","]":"[","}":"{","*)":"(*",")":"("} 
    for line in fileToOpen:
        if(line.isspace()):
            break

def is_nested(line):    
        bracUsed = []
        #openChar
        num = 0
        count=0
        while(num < len(line)):
                if line[num] in "(<[{":
                    if line[num+1] == "*" and line[num]=="(":
                       bracUsed.append("(*")
                       num = num + 2
                       
                    else:
                        bracUsed.append(line[num])
                        num +=1
                    count +=1

                elif line[num] in ">}]*)":
                    if line[num]=="*" and line[num+1]==")":
                        
                        index = "*)"
                        num += 2
                    elif(not line[num] == "*"):
                        index = line[num]
                        num +=1
                    else:
                        count += 1
                        num += 1
                        continue
                    count += 1    
                    
                    if bracUsed[-1] == charDict[bracUsed]:

                        bracUsed.pop(-1)
                    else:
                        fileToWrite.write("NO "+str(count)+"\n")
                        break
                else:
                    num += 1
                    count += 1
  
        
        if(not bracUsed):
            fileToWrite.write("YES\n")
        elif(bracUsed and len(line)== count):
            fileToWrite.write("NO "+str(count)+"\n")
        

            
              

if __name__ == '__main__':
    main(sys.argv)