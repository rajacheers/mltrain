def Fibonacci(n):
    
    a, b = 0, 1
    
    for x in range(0,n):
        print(a)
        a, b = b, a + b 
    
Fibonacci(10)
