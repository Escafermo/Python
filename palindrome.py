def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]