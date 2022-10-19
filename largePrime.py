import random
import time
import libnum

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
            b = (b**2) % number_to_test #Write b as b^2 mod number_to_test
            if b == b-1: #Checks if b is equal to b-1
                break #If so, break out of loop, return True
        else:
            return False #Else, number is composite

    return True #Number can be prime

def solovoy_strassen(number_to_test, iterations):
    for _ in range(iterations):
        # Generate a random number a
        a = random.randint(2,number_to_test - 1)
        jacobian_number = libnum.jacobi(a,number_to_test)
        mod = pow(a, (number_to_test-1)//2, number_to_test) #a^(n-1)/2 mod n
       
        if ((jacobian_number == 1 and mod == 1) or (jacobian_number == -1 and mod == number_to_test - 1)):
            return True
 
    return False

iterations = 50
tested_number = generate_odd_number()
prime_list = []

while len(prime_list) < 2:
    miller_rabin_check = miller_rabin(tested_number, iterations) 
    if miller_rabin_check:
        solovoy_strassen_check = solovoy_strassen(tested_number, iterations)
        if solovoy_strassen_check:
            print("Miller-Rabin: ", miller_rabin_check)
            print("Solovay-Strassen: ",solovoy_strassen_check)
            print("Passed both tests: ",tested_number, "\n")
            prime_list.append(tested_number)
     
    tested_number = generate_odd_number()


for i in range(len(prime_list)):
    start_time = time.time()
    miller_rabin(prime_list[i], iterations)
    print("Miller-Rabin time:")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time() 
    solovoy_strassen(prime_list[i], iterations)
    print("Solovay-Strassen time:")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
