# # Сначала вводится число N,затем вводится ровно N целых чисел. Подсчитайте,сколько из них равны нулю,и выведите это количество
n = int(input())
count = 0
for i in range(n):
    a = int(input())
    if a == 0:
        count +=1
    else:
        count += 0
print(count)

# ##  zdaniya 2
# ## Вводится натуральное число X.Подсчитайте количество натуральных делителей числа X(включая 1 и само число).x≤2e9(2миллиарда)
x = int(input())
count = 0
for i in range(1, x+1):
    if x % i == 0:
          count += 1

print(count - 2)

## Вводятся целые числа A и B. Гарантируется,что A≤B .Выведите все четные числа на заданном отрезке через пробел

a = int(input())
b = int(input())
if a % 2 == 0:
     a += 1
     for i in range(a, b, 2):
          print(i)
else:
     for i in range(a, b, 2):
          print(i)





