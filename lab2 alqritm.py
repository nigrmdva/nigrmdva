a = [0] * int(input('Elementlərin sayı: '))
k = 0

# Massivin doldurulması
for i in range(len(a)):
    a[i] = int(input())

print('A:', a)

# 9-dan böyük elementlərin cəmini hesablamaq
sum_of_elements_greater_than_9 = 0
for x in a:
    if x > 9:
        sum_of_elements_greater_than_9 += x

print("9-dan böyük elementlərin cəmi:", sum_of_elements_greater_than_9)