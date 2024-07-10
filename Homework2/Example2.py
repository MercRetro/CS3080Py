#Mercury Goodwin
#Proof of List

#remove space from input
def removeSpace(list):
   return [item.lstrip() for item in list]

#check if int
def isInt(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

#input and formating
commaStr = input ("Enter a comma separated list of integers, doubles, and strings:")
unformatedList = commaStr.split(",")
formatedList = removeSpace(unformatedList)

#print list
print(formatedList)

#print if int
for item in formatedList:
   if (isInt(item)):
      print(item, "is an integer")
      