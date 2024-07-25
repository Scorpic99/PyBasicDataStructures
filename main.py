#  "1st program"
print((9 ** 0.5) * 5)

#  "2nd program"
print(9.99 > 9.98 and 1000 != 1000.1)

#  "3rd program"
num = 1234
num2 = 5678

count = num // 10
count = count % 100

count2 = num2 // 10
count2 = count2 % 100

print(count + count2)

#  "4th program"
num = 13.42
num2 = 42.13

leftPartN1 = int(num)
temp = num * 100
rightPartN1 = int(temp) % 100

leftPartN2 = int(num)
temp = num * 100
rightPartN2 = int(temp) % 100

print(leftPartN1 == leftPartN2 or leftPartN1 == rightPartN2 or rightPartN1 == rightPartN2)


