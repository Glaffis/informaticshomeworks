a = input()
l = list(a)
flipped_list = l[::-1]
if l == flipped_list:
    print(a, ' is a regular palindrome')
else:
    print(a, ' is not a palindrome')