for i in range(2,301):
    Is_prime = True #假设条件成立
    for j in range(2,i):
        if i % j == 0:
            Is_prime = False
    #else:
    #    print(f"{i}是素数")
    if Is_prime:
        print(f"{i}素数")