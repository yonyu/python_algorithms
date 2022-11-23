def gcd(x, y):
    """Find greatest common denominator (GCD) of two integers

    Args:
        x (_int_): the first integer
        y (_int_): the second integer

    Returns:
        _type_: the greatest common denominator
    """
    
    while y != 0:
        t = x
        x = y
        y = t % x
        
    return x
        

print('should print 12:')
print(gcd(60, 96))  # 12    
print('should print 4:')    
print(gcd(20, 8)) # 4
print('should print 8:')    
print(gcd(8, 0)) # 4