#Mercury Goodwin
#HW2

#remove space from input
def removeSpace(list):
   return [item.lstrip() for item in list]

#get original type
def whatType(s):
    if type(s).__name__ == "int":
        return "integer"
    elif type(s).__name__ == "str":
        return "string"
    elif type(s).__name__ == "float":
        return "float"
    else:
        return "idk"

#check if int/ float
def isInt(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
def isFloat(s):
    try:   
        float(s)
    except ValueError:
        return False
    else:
        return True
def isString(s):
    try:
        str(s)
    except ValueError:
        return False
    else:
        return True

#input and formating
commaStr = input ("Enter a comma separated list of integers, doubles, and strings:")
unformatedList = commaStr.split(",")
formatedList = removeSpace(unformatedList)

#print list

if formatedList and formatedList != ['']:
    print(formatedList)
    for item in formatedList:
        print(item)
        print(whatType(item))
    print()
    for item in formatedList:
      if (isInt(item)):
         item = int(item)
         print(item, "is an integer")
      elif (isFloat(item)):
         item = float(item)
         print(item, "is a float")
      elif (isString(item)):
         print(item, "is a string")
      else:
         print("is a secret fourth thing")

else:
   print ("List is empty")
      