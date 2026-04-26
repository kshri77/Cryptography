def primality_test(n): 
    print("\n--- Primality Testing ---") 
    #print("Formula: n mod i ≠ 0 for all 2 ≤ i ≤ √n\n") 
    if n <= 1: 
        print(f"{n} is NOT a prime number") 
        return 
    step = 1 
    for i in range(2, int(math.sqrt(n)) + 1): 
        print(f"Step {step}:") 
        print(f"Check: {n} mod {i}") 
print(f"{n} mod {i} = {n % i}\n") 
        if n % i == 0: 
            print(f"{n} is NOT a prime number") 
            return 
        step += 1 
    print(f"{n} is a PRIME number")
