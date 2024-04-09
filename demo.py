def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return fibonacci(i - 1) + fibonacci(i - 2)
    else:
        raise Exception
    
def isPalindrome(s: str):
    s = s.lower()
    s = ''.join(s.split())
    r = s[::-1]
    palindrome = (s == r)
    return palindrome

def mysteryFunction(x):
    return x + 5