# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13

a = 0
b = 1
n = 7
print(a)
print(b)
for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c
