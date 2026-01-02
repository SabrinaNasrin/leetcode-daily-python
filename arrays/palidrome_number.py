def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Test
print(is_palindrome(454))  #True
print(is_palindrome(-555)) #False
print(is_palindrome(102))   #False
