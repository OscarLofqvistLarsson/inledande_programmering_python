def is_palindrome(s):
    return s == s[::-1]

s = str(input("input a string") )
s.lstrip(" ")
s.lower()


i = is_palindrome(s)

print(s)

if i:
    print(s,":Is an palindrome")

else:
    print(s,":Is not an palindrome")