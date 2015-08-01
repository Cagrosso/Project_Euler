#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#using method 2 http://www.wikihow.com/Factor-a-Number

def factors(lowest, num):
    #lowest being the current lowest factor, num being the current value after factoring the num
    factor = []
    if(num == 1):
        # if num is 1, then all factors found
        return factor
    elif(num % lowest == 0):
        #if the lowest factor still neatly divides num, rerun factors with new num and current lowest factor
        factors(lowest, num/lowest)
    else:
        for i in range(lowest, num):
            #searchs for factors between current lowest and num of num
            if(num % i == 0):
                #if num is evenly divided, add i to factor and rerun factors
                factor.append(i)
                factors(i,num/i)


def fact(num):
    return factors(2, num)

print(fact(6552))
