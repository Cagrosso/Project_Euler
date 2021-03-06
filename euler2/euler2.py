#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib_to(n):
    fib = [0,1]
    for i in range(2, n+1):
        x = fib[i - 1]
        y = fib[i - 2]
        #print("This is round %d: %d + %d" % (i, x, y)) #debug
        fib.append(x + y)
    return fib

def is_even(list):
    even = []
    for i in range(0, len(list)):
        if(list[i] % 2 == 0):
            even.append(list[i])
    return even

#33 gives the largest fibonacci number before 4 million

fib = fib_to(33)
print("Sum: %d" % sum(is_even(fib)))
