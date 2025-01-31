# def fibonacci_sum(n):
#     if n <= 0:
#         return 0

    
#     def fibonacci(n):
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a

    
#     return fibonacci(n + 2) - 1

# terms = int(input("Enter the number of terms in the Fibonacci series: "))
# result = fibonacci_sum(terms)
# print(f"The sum of the first {terms} terms of the Fibonacci series is: {result}")
def fibonacci (n):
    first = 0
    second = 1
    sum = 0
    
    for i in range (n):
        sum += first
        temp = first
        first = second
        second = first + temp
    
    return sum
        
print(fibonacci(10))