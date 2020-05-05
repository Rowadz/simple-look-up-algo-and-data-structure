def get_fib(pos):
    if pos == 0 or pos == 1: return pos
    return get_fib(pos - 1) + get_fib(pos - 2)