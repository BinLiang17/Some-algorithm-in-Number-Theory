import math

# The list of all prime factories of this number    
list_p = []

# We can use this function to judge if the number is prime
def judge_p(number:int) :
    if number == 2:
        return(True)
    for i in range(2,number) :
        if number % i == 0:
            return(False)
    return(True)

# Use this function, we can get a list of all the primes
# which we want to do factorisation.
def getProduct(num):
    
    # If this number is prime, finish, store it in our list
    if judge_p(num):
        list_p.append(num)
    # If not, we will do factorisation on it
    else:
        i = 2
        while i <= int(math.sqrt(num)) + 1 :
            if num % i == 0:
                if judge_p(i):
                    list_p.append(i)
                    r = int(num / i)
                    # We will do iteration untill all the factoris are prime number
                    # By the fundamental theorem of arithmetic and divisors
                    # We know that the experission is unique.
                    # So, we can start at any prime number
                    getProduct(num = r)
                    break
            i += 1
            
# We will use this function to do all the works
def prime_fac():

    # Let user to input the number.
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please input an integer ! Let's try again ! ")
        prime_fac()
    
    getProduct(abs(number))
    # We will use a dictionary to store the primes and their power.
    dic_p = {}
    
    # Give a initial value for all the keys
    for prime in list_p:
        dic_p[prime] = 0
        
    # Count the power of all the prime
    for prime in list_p:
        dic_p[prime] += 1
    equation = ''
    
    # Because we use the absolute before...
    if number/abs(number) == 1:
        sign = ''
    else:
        sign = '-'
    
    # To sum up
    for item in dic_p:
        equation = equation + str(item) + "^(" + str(dic_p[item]) + ')'
    equation = str(number)+' = ' + sign + equation
    # Output the factorisation result.
    print(equation)
    
    return(dic_p)
   
while True:
    prime_fac()
    signal = input("Do you want to quit? Press '1' to quit. Press 'Enter' to one more times.")
    if signal == '1':
        print('We quit the program')
        break
    # Clean the list, then we can use it again
    list_p = []
        

