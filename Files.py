#For coding contests that have a sample input with a desired outcome to test code instead of manually entering your inputs each time you can use a input file
#You can do this in contests to save time using pythons file manipulation commands

#file = open("Inputs.txt","w+") → "w+" creates a file
#file.write("You can use this to automate inputs in a contest")
#file.close()

#file = open("Inputs.txt","r") → "r" opens the file in read mode
#inp = file.read() → Read reads the entire file

#print(inp)
#This is how you would set it up if you would like to creat and read the input file in python

##Sample using an actual problem

file = open("2015S1.txt", "r")

i = int(file.readline()) #→ Readline reads one line of the file at a time
statement = []

for num in range(i):
    profit = int(file.readline())
    if profit == 0:
        statement.pop()
    else:
        statement.append(profit)

total = 0
for i in range(len(statement)):
    total = total + statement[i]

print (total)

