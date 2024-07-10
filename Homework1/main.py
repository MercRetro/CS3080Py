import homework1

#user validation
while True:
  try:
    user_input_one = float(input("Enter a number: "))
  except ValueError:
    print("Not a number, try again")
  else:
    break
  
while True:
  try:
    user_input_two = float(input("Enter a 2nd number: "))
  except ValueError:
    print("Not a number, try again")
  else:
    break


#add, subtract, multiply, and divide the two inputs
sum = homework1.sum(user_input_one,user_input_two)

sub = homework1.sub(user_input_one,user_input_two)

mul = homework1.mul(user_input_one,user_input_two)

div = homework1.div(user_input_one,user_input_two)

#print to console
print("Sum:  "+str(user_input_one) + " + " + str(user_input_two)+" = " 
      +str(sum))

print("Sub:  "+str(user_input_one) + " - " + str(user_input_two)+" = " 
+str(sub))

print("Mul: "+str(user_input_one) + " * " + str(user_input_two)+" = " 
+str(mul))

print("Div:  "+str(user_input_one) + " / " + str(user_input_two)+" = " 
+str(div))
