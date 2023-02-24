"""
1-misal. a ham b sanlar berilgen (a<b). a dan b ga deyin bolgan
sanlardin kvadratlarinin qosindisin esaplawshi programma duzin.
"""
# a = int(input("A: ")) # 3
# b = int(input("B: ")) # 7
# kv = 0

# for i in range(a, b): # 3, 4, 5, 6
#     kv += i**2        # 9, 25, 50, 86
# print(f"{a} ham {b} arasi kv qosindisi: {kv}")

# a = int(input("A: ")) # 3
# b = int(input("B: ")) # 7
# kv = 0 # 9, 25, 50, 86

# while a < b: # True, True, True, False
#     kv += a ** 2
#     a += 1
# print(f"{a} - {b} kv: {kv}")


"""
2-misal. n putin sani berilgen (n > 0). Tomendegi qosindini esaplawshi 
programma duzilsin.
S = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n
"""
# n = int(input("N: "))  # 5
# S = 0

# for i in range(1, n+1):
#     S += 1 / i
# print(f"S = {S}")


# n = int(input("N: ")) # 5
# S = 0
# i = 1

# while i < n+1:
#     S += 1 / i
#     i += 1
# print(f"S = {S}")
"""
3-misal. n putin sani ham a haqiyqiy sani berilgen (n>0). a nin
n-darejesin esaplawshi programma duzilsin.
"""
# a = int(input(" a ni kiritin "))
# n = int(input(" b ni kiritin "))
# for i in range(n+1):
#     b = a ** i
# print(b)

# a = int(input(" A: "))
# n = int(input(" N: "))
# i = 1
# while i < n:
#     p = a ** i
#     i += 1
# print(p)

"""
4-misal. N ham K sanlari berilgen. Tomendegi qosindini esaplan.
1^K + 2^K + ... + N^2
"""
# n = int(input(" N: "))
# k = int(input(" K: "))
# s = 0
# for i in range(1, n):
#     s = s + i ** k
# print(s)

# n = int(input(" N: "))
# k = int(input(" K: "))
# s = 0
# i = 1
# while i < n:
#     s = s + i ** k
#     i += 1
# print(s)
"""
5-misal. N putin sani berilgen. Tomendegi qosindini esaplawshi
programma jazin. 1^1+2^2+3^3+...N^N.
"""
# n = int(input(" N: "))
# s = 0
# for i in range(n):
#     s = s + i*i
# print(s)

# n = int(input(" N: "))
# s = 0
# i = 1
# while i < n:
#     s = s + i*i
#     i += 1
# print(s)
"""BREAK OPERATORI"""
# i = 0
# while True: # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#     if i > 10:
#         break
#     i += 1
#     print("Salem")

# n = int(input("N: "))
# jup_sanlar = []

# for i in range(0, n, 2):
#     jup_sanlar.append(i)
# print(jup_sanlar)

# n = int(input("N: "))
# jup_sanlar = []
# i = 0

# while i < n:
#     if i % 2 == 0:
#         jup_sanlar.append(i)
#     i += 1
# print(jup_sanlar)


"""CONTINUE OPERATORI"""
# n = int(input("N: "))  # 5
# jup_sanlar = []
# i = -1
#
# while i < n:
#     i += 1
#     if i % 2 == 1:
#         continue
#     jup_sanlar.append(i)
# print(jup_sanlar)




















