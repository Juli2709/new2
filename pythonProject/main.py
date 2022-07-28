import random
p = 0
a = int(input("введите 1 число от 1 до 20: "))
b = int(input("введите 2 число от 1 до 20: "))
c = random.randint(1, 20)
d = random.randint(1, 20)
print("третье число: ", c)
print("четвертое число: ", d)
sum1 = a + b
sum2 = c + d
print(" ", sum1)
print("сумма рандомных чисел: ", sum2)

while p <= 7:
    p = p + 1
    continue
if sum1 > sum2:
    print("введенные больше")
else:
    print("рандомные больше")




