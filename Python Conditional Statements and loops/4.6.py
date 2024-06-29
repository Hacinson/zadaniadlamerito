def fibonacci_series():
    a, b = 0, 1
    
    print(a)
    print(b)
    
    while True:
        c = a + b
        
        if c > 50:
            break
        
        print(c)
        
        a = b
        b = c

fibonacci_series()
