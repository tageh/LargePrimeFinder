import random
import time

prime_candidate = 2359387295841603593872497896878874911354964981437788423001084377685944959437718053927835500869359979283068184632251708346109938684331052172298133038997763758508710452918070355313179108348018708020045284488899366383442690192063712113658805209824845665266206807184787493604374694215753343981094706853471784559

def generate_odd_number():
    big_number = random.getrandbits(1024)
    if (big_number % 2) != 0:
        odd = big_number
    else:
        odd = big_number + 1
    return odd

def miller_rabin(number_to_test, iterations):
    u = number_to_test - 1
    k = 0

    while (u % 2 == 0):
        u //= 2
        k += 1
    
    for _ in range(iterations):
        a = random.randint(2, number_to_test-2) #math.sqrt(number_to_test) faster?
        b = pow(a,u,number_to_test)

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
tested_number = generate_odd_number()

start_time = time.time()

print(miller_rabin(prime_candidate, 50))
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

