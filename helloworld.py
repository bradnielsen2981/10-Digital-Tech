print("Hello World") #calls the print function
name = "Mr Nielsen" #string - string of char
numberofapples = 0 #integer  
costperapple = 0.5 #float - floating point
isapplerotten = True #boolean - 0 or 1
letter = 'A' #char - 1 byte

message = "Welcome " + name  #adding strings together
print(message)
numberofapples = input("Please enter the number of apples: ")
numberofapples = int(numberofapples)
total = numberofapples * costperapple
print("Your total = " + str(total))

#Type error - you are using the wrong data type

#The above variables exist in the Global Namespace