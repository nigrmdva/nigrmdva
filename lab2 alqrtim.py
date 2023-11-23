
import random

# Massivin uzunluğunu təyin etmə
n = int(input('Elementlərin sayı: '))
a = [random.randint(1, 20) for _ in range(n)] # 1-20 arasında təsadüfi qiymətlər
 
print('A:', a)

# 9-dan böyük elementlərin cəmini hesablamaq
sum_of_elements_greater_than_9 = 0
for x in a:
    if x > 9:
        sum_of_elements_greater_than_9 += x

print("9-dan böyük elementlərin cəmi:", sum_of_elements_greater_than_9)
