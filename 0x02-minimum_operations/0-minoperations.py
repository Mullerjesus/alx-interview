#!/usr/bin/python3  

def minOperations(n):  
    if n <= 1:  
        return 0  
    
    operations = 0  
    factor = 2  
    
    while n > 1:  
        if n % factor == 0:  
            operations += factor  
            n //= factor  
        else:  
            factor += 1  
            
    return operations  

if __name__ == "__main__":  
    # Test cases  
    n = 4  
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 4  

    n = 12  
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 7  

    n = 9  
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 6
