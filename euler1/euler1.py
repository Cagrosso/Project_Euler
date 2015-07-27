#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
multiples = []
total = 0;

print("Finds the sum of all multiples of 3 or 5 below a max number. \n")
limit = input("Max number? ")

def isMult(x):
    if(x % 3 == 0 or x % 5 == 0):
        return True
    else:
        return False

#print('3: ', isMult(3))
#print('4: ', isMult(4))
#print('5: ', isMult(5))

for i in range(0, int(limit)):
    if(isMult(i)):
        multiples.append(i)

for i in range(0, len(multiples)):
    total += i
