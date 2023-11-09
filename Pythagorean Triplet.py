import time
def triplet(num1, num2, num3):
    list1 = [num1, num2, num3]
    list1.sort()
    sum_calc = (list1[0]**2) + (list1[1]**2)
    if sum_calc == (list1[-1]**2):
        return True
    else:
        return False
    
num1 = int(input("Enter a number:\n"))
num2 = int(input("Enter another number:\n"))
num3 = int(input("And another number (Last one I swear):\n"))
print("And ANOTHE- just kidding")
time.sleep(1.5)
print(triplet(num1, num2, num3))
