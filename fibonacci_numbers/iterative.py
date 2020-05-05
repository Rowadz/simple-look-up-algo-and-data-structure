def get_fib(pos):
    if pos == 0: return 0
    if pos == 1: return 1
    first = 0
    second = 1
    next = first + second
    for i in range(2, pos):
        first = second
        second = next
        next = first + second
    return next

print(get_fib(1))
print(get_fib(2))
print(get_fib(3))
print(get_fib(4))
print(get_fib(5))
print(get_fib(6))