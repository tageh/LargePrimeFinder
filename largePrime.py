import random
import time
import math

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

        if (b == 1 or b == (number_to_test-1)): #If base^u mod number_to_test is equal to 1 or number_to_test-1 continue loop
            continue
        
        for _ in range(k-1):
            b = (b^2) % number_to_test #Write b as b^2 mod number_to_test
            if b == b-1: #Checks if b is equal to b-1
                break #If so, break out of loop, return True
        else:
            return False #Else, number is composite

    return True #Number can be prime

def modulo(base, exponent, mod):
    x = 1;
    y = base;
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod;

        y = (y * y) % mod;
        exponent = exponent // 2;

    return x % mod;

def jacobian(a,number_to_test):
    if (a == 0):
        return 0;# (0/n) = 0
 
    ans = 1;
    if (a < 0):
         
        # (a/n) = (-a/n)*(-1/n)
        a = -a;
        if (number_to_test % 4 == 3):
         
            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans;
 
    if (a == 1):
        return ans; # (1/n) = 1
 
    while (a):
        if (a < 0):
             
            # (a/n) = (-a/n)*(-1/n)
            a = -a;
            if (number_to_test % 4 == 3):
                 
                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans;
 
        while (a % 2 == 0):
            a = a // 2;
            if (number_to_test % 8 == 3 or number_to_test % 8 == 5):
                ans = -ans;
 
        # swap
        a, number_to_test = number_to_test, a;
 
        if (a % 4 == 3 and number_to_test % 4 == 3):
            ans = -ans;
        a = a % number_to_test;
 
        if (a > number_to_test // 2):
            a = a - number_to_test;
 
    if (number_to_test == 1):
        return ans;
 
    return 0;

def solovoy_strassen(number_to_test, iterations):
 
    if (number_to_test < 2):
        return False;
    if (number_to_test != 2 and number_to_test % 2 == 0):
        return False;
 
    for _ in range(iterations):
         
        # Generate a random number a
        a = random.randrange(number_to_test - 1) + 1;
        jacobian_number = (number_to_test + jacobian(a, number_to_test)) % number_to_test;
        mod = modulo(a, (number_to_test - 1) / 2, number_to_test);
 
        if (jacobian_number == 0 or mod != jacobian_number):
            return False;
 
    return True;

iterations = 100
i = 0
#tested_number = generate_odd_number()
try_number = 2359387295841603593872497896878874911354964981437788423001084377685944959437718053927835500869359979283068184632251708346109938684331052172298133038997763758508710452918070355313179108348018708020045284488899366383442690192063712113658805209824845665266206807184787493604374694215753343981094706853471784559

start_time = time.time()
print(miller_rabin(try_number,50))
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


