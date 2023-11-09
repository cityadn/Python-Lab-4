def calculation(three_digits):
    first_num = int(three_digits[0])
    second_num = int(three_digits[1])
    third_num = int(three_digits[2])
    calc = (first_num**3) + (second_num**3) + (third_num**3)
    print("sum =",calc)
    if calc == int(three_digits):
        return "It's an Armstrong number"
    else:
        return "It's not an Armstrong number"  

three_digits = input("Enter a number of 3 digits:\n")
while len(three_digits) != 3:
    three_digits = input("Enter a number of 3 digits:\n")
print(calculation(three_digits))




