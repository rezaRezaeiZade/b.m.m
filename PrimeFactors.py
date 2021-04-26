# B.M.M in 600851475143 chie?(in masaleye sevome euler hast)
l_primeFactors = []
# amel haye avale tooye damane-ye moshakhas shode ro peida mikone
def primeFactors():
    for i in range(1, 20):
        #print("--------\ni = ", i) #to debug
        control = 0
        for n in range(1, 20):
            #print("n = " ,n) #to debug
            if i % n == 0:
                #print(f"{i} % {n} = 0") #to debug
                control += 1
                #print(f"control is {control}") #to debug
        if control == 2 or control == 1:
            l_primeFactors.append(i)
            #print(f"{i} was appended") #to debug


specificPrime = []
# amel haye avale adade dade shode ro peida mikone
def detect(n):
    for i in l_primeFactors:
        if n % i == 0:
            specificPrime.append(i)


a = int(input("Emter the number "))
primeFactors()
detect(a)
print(f"The largest prime factor of {a} is ", specificPrime[-1])
