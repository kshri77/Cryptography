import math 
def euclidean_algorithm(a, b): 
    print("\n--- Euclidean Algorithm (GCD) ---") 
    print("Formula: gcd(a, b) = gcd(b, a mod b)\n") 
    step = 1 
    while b != 0: 
        print(f"Step {step}:") 
        print(f"gcd({a}, {b})") 
        #print(f"{a} = {b} × {a // b} + {a % b}") 
        print(f"gcd({b}, {a % b})\n") 
        a, b = b, a % b 
        step += 1 
    print("Final Step:") 
    print(f"gcd({a}, 0)") 
    print(f"GCD = {a}") 
