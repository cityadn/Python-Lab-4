def reverse(four_digit):
    num = four_digit
    new_num = num[3] + num[2] + num[1] + num[0]
    return new_num

four_digit = input("Enter a four digit number:")
while len(four_digit) != 4:
    four_digit = input("Enter a four digit number:")
print(reverse(four_digit))
