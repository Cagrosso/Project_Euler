#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
multiples = []
total = 0;

print("Finds the sum of all multiples of 3 or 5 below a max number. \n")
limit = int(input("Max number? "))

def isMult(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

#print('3: ', isMult(3))
#print('4: ', isMult(4))
#print('5: ', isMult(5))
#print('6: ', isMult(6))
#print('7: ', isMult(7))
#print('8: ', isMult(8))
#print('9: ', isMult(9))

for i in range(0, limit):
    if(isMult(i)):
        multiples.append(i)

total = sum(multiples)

print("The sum of all multiples of 3 or 5 in %d is %d" % (limit, total))
