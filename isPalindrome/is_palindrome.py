def is_palindrome_1(s: str) -> bool:
    return s == s[::-1] 

print(is_palindrome_1('aaa'))
print(is_palindrome_1('abc'))

def is_palindrome_2(s: str) -> bool:
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]: return False
    return True


print(is_palindrome_2('aaa'))
print(is_palindrome_2('abc'))
