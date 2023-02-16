
# create a function that takes a number and outputs all the primes up to the number chosen
def getprimes(number):
    primelist = [2]
    if number < 2:
        return
    elif number == 2:
        print(2)
        return
    else:
        print(2)
        for i in range(3,number+1):
            isprime = True
            for prime in primelist:
                if (i%prime) == 0:
                    isprime = False
                    break  #breaks out of the for loop
            if isprime:
                print(i)
                primelist.append(i) #add number to primelist
    return

a = input("Enter the number: ")
a = int(a)
getprimes(a)

