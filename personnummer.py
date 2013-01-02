#!/usr/bin/python
""" Module for validating if a given swedish social security number
is valid or not."""
___author___ = "Riccard Akerman"
___version___ = "0.1"

def ValidateSN(x):
  count=1
  value=0
  """ Function will accept social secrity number in form of yymmddxxxx"""
  pnlist = str(x)
  for sd in pnlist:
    if((count % 2) == 1):
      count += 1  
      needSplit = str((int(sd) * 2))
      if((len(needSplit)) == 2):
        for ns in needSplit:
           value += (int(ns))
      else:
        value += (int(ns))
    elif((count % 2) == 0):
      count += 1  
      value += (int(sd))
  """ Return value is 0 for true and 1 for false """
  print ((value % 2))
  if((value % 2) == 0):
    print "DEBUG: True"
    return "0"
  else:
    print "DEBUG: False"
    return "1"
def CreateCN(x):
  count=1
  value=0
  ten=0
  """ Function will accept soical security number in form of yymmddxxx"""
  pnlist = str(x)
  for sd in pnlist:
    if((count % 2) == 1):
      count += 1  
      needSplit = str((int(sd) * 2))
      if((len(needSplit)) == 2):
        for ns in needSplit:
           value += (int(ns))
      else:
        value += (int(ns))
    elif((count % 2) == 0):
      count += 1  
      value += (int(sd))
  while True:
    if(ten >= value):
      print (ten - value)
      print "DEBUG: ", value
      break
      
    ten += 10 
