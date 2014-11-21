def mcnuggets(n):
    divisors = (20, 9, 6)
    
    for idx, d in enumerate(divisors):
        rem = n % d 
        if rem == 0:
            return True
        elif rem < divisors[-1]:
            continue
            
        for d1 in divisors[idx:]:
            rem = rem % d1
            if rem == 0:
                return True
            elif rem < divisors[-1]:
                continue

    return False
        
for i in range(50):
    print i, mcnuggets(i)
