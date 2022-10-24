import random
import time
import libnum #Library used for jacobi function (pip install libnum)

def generate_odd_number():
    big_number = random.getrandbits(1024) #Generate random 1024 bit number
    
    while big_number.bit_length() != 1024: #Make sure number is 1024 bit
        big_number = random.getrandbits(1024)

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
        a = random.randint(2,number_to_test - 1) #Generate random a to test with
        jacobi = libnum.jacobi(a,number_to_test) #Find the Jacobi number for number to be tested
        mod = pow(a, (number_to_test-1)//2, number_to_test) #a^(n-1)/2 mod n
       
        if ((jacobi == mod) or (jacobi == -1 and mod == number_to_test - 1)): #Checks congruence between a^(p-1)/2 and (a/p) (mod p)
            continue #Continue if condition is true
        else:
            return False #Number is composite
 
    return True #Number can be prime

iterations = 50 #Sets number of iterations
tested_number = generate_odd_number() #Generate random number to test
prime_list = [] #List to store found numbers in
numbers_tested = 0
#Automation proceess to find possible prime numbers

while len(prime_list) < 2: #Loops through numbers till it finds two "primes"
    miller_rabin_check = miller_rabin(tested_number, iterations) #Runns number through Miller-Rabin algorithm
    if miller_rabin_check: #If the passes Miller-Rabin 
        solovoy_strassen_check = solovoy_strassen(tested_number, iterations) #Tests Solovay-Strassen algorithm
        if solovoy_strassen_check: #If the number passes both algorithms, it has a high probability of begin prime
            print("Miller-Rabin:", miller_rabin_check) #Print outcome of Miller-Rabin test
            print("Solovay-Strassen:",solovoy_strassen_check) #Print outcome of Solovay-Strassen test
            print("Passed both tests:",tested_number, "\n") #Print number that has passed both tests
            prime_list.append(tested_number) #Addes the number to the list
     
    tested_number = generate_odd_number() #Generate new random number to be tested
    numbers_tested += 1


#Automated proceess to time numbers found in previus step

for i in range(len(prime_list)): #Loops through the length of the list
    start_time = time.time() #Starts timer
    miller_rabin(prime_list[i], iterations) #Runns through Miller-Rabin algorithm
    print("Miller-Rabin time:")
    print("--- %s seconds ---" % (time.time() - start_time)) #Prints time it took for Miller-Rabin

    start_time = time.time() #Starts time
    solovoy_strassen(prime_list[i], iterations) #Runns through Solovay-Strassen algorithm
    print("Solovay-Strassen time:")
    print("--- %s seconds ---" % (time.time() - start_time)) #Prints time is took for Solovay-Strassen
    print("\n")

print("Total numbers tested:", numbers_tested)
