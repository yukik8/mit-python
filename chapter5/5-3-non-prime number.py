def non_prime(num):
    return [x for x in range(2,num+1) 
    if not all(x%y!=0 for y in range(2,x))]
print(non_prime(100))