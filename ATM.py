x = 1000
y = 0
z = 0
A = 0
w = 0
d = 0
T = 0
F = 0
P = 0
# Password:
P = input("Enter Password")
if P != 'Hi' :
     print("Wrong password")
     exit()
while A == 0 :
  
  print(""" \
  "Welcome to the ATM"
  1.Check Balance
  2.Deposit Money
  3.Withdraw Money
  4.Exit
        """
  )
  y = input("choose an action by entering its number")

# Warning:
  if F == 3 :
    print("Warning you have failed 3 withdrawls")

# Display balance:
  if y == '1' :
      print("Current balance is:",x)

# Deposit:
  elif y == '2' :
     d = int(input("How much do you want to deposit?"))
     if d < 0 :
        print("you entered an invalid amount")
        break
     else:
        x += d
     print("New balance is:",x)
# Transaction counter:
     T += 1

# Withdraw:
  elif y == '3' :
     z = int(input("How much do you want to Withdraw?"))
# Validate input:
     if w < 0 :
        print("you entered an invalid amount")
        break

     if z <= x :
        x -= z
        print("New balance is:",x)
        T += 1
     else:
        print("You cant withdraw This much")
#Failed counter:
        F += 1

# Exit:
  elif y == '4' :
     print("Number of transactions:",T)
     break
