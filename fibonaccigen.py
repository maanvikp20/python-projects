import time
start_time = time.time()

# Memoization dictionary
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    memo[n] = result
    return result

    
for i in range(1):
    print(fibonacci(i))
    
print("--- %s seconds ---" % (time.time() - start_time))