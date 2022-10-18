import random
import time

def generate_odd_number():
    big_number = random.getrandbits(1024) #Generate random 1024 bit number
    if (big_number % 2) != 0: #Checks if number is odd
        odd = big_number
    else:
        odd = big_number + 1 #If it's not odd, make it odd
    return odd #Return odd number

def miller_rabin(number_to_test, iterations):
    #Find u odd such that number_to_test-1 = 2^k * u 
    u = number_to_test - 1 
    k = 0
    while (u % 2 == 0): #While u is even
        u //= 2 #Factoring out powers of 2 from number_to_test-1
        k += 1 #k is numbers of factorings done 

    for _ in range(iterations):
        base = random.randint(2, number_to_test-2) #Generate random base to test with
        b = pow(base,u,number_to_test) #b = base^u mod number_to_test 

        if (b == 1 or b == (number_to_test-1)):
            continue
        
        for _ in range(k-1):
            b = b*b % number_to_test
            if b == b-1:
                break
        else:
            return False

    return True


iterations = 100
i = 0
#tested_number = generate_odd_number()

start_time = time.time()

print(miller_rabin(97,100))
print("--- %s seconds ---" % (time.time() - start_time))

'''
while i < 1000:
    print(miller_rabin(tested_number, iterations))
    prime_check = miller_rabin(tested_number, iterations) 
    if prime_check == True:
        print(tested_number)
        break
    tested_number = generate_odd_number()
    i += 1
'''


