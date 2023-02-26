"""
# 1-MASELE Ushnuyeshliktin maydanin ham perimetrin tabin?
import math
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
a = float(a)
b = float(b)
c = math.sqrt(a**2 + b**2)
S = (a * b)/2
P = a + b + c
print("Ulken tarepi", int(c))
print("Maydani", int(S))
print("Perimetri", int(P))

# 2-MASELE Kvadrat tenlemenin korenlerin tabin
import math
print("a*x+b*c+c=0")
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
c = int(input(" c ni kiritin "))
disc = b ** 2 - 4 * a * c
if disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print(f"Eki koreni bar {int(x1), int(x2)}")
elif disc == 0:
    x = (-b) / (2 * a)
    print(f"Bir koreni bar {x}")
else:
    print("Koreni joq")
# 1-MASELE
a = int(input(" a = "))
b = int(input(" b = "))
print(a+b)
# 2-MASELE
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
if a == b:
    print(f"{a} = {b}")
else:
    print("Programma toqtadi")
# 3-MASELE
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
if a < b:
    print(f"{a} < {b}")
else:
    print("Programma toqtadi")
# 4-MASELE
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
if a > b:
    print(f"{a} > {b}")
else:
    print("Programma toqtadi")
# 5-MASELE
myfile = open("Hello.txt", "w+")
a = int(input(" a ni kiritin "))
b = int(input(" b ni kiritin "))
myfile.write(f"{a+b}")
myfile.close()
# 6-MASELE
myfile1 = open("input.txt", "w+")
a = int(input(" a ni kiritin "))     # 2
b = int(input(" b ni kiritin "))     # 3
myfile1.write(f"{a}  {b}")
myfile2 = open("output.txt", "w+")
myfile2.write(f"{a*b}")              # 6
myfile2.close()
# 7-MASELE
myfile1 = open("input.txt", "w+")
a = int(input(" a ni kiritin "))     # 4
b = int(input(" b ni kiritin "))     # 2025
myfile1.write(f"{a}  {b}")
myfile2 = open("output.txt", "w+")
myfile2.write(f"{a*b}")              # 8100
myfile2.close()
# 8-MASELE
myfile1 = open("input.txt", "w+")
x = int(input(" x ti kiritin "))
y = int(input(" y ti kiritin "))
z = int(input(" z ti kiritin "))
if (-10) ** 9 <= z <= 10 ** 9:
        myfile1.write(f"{z} kiritildi")
myfile2 = open("output.txt", "w+")
if x <= y:
    myfile2.write(f"{x, y} jupliqlari \n{x*y == z}")
else:
    print("Eger sheksiz bolsa", -1)

9-MASELE
a = 10
b = 8
a = b ^ a
b = a ^ b
a = a ^ b
print(b)
print(a)

# 10-MASELE
# l = int(input("L: "))
# M = l // 100
# print(f"{M} metr")

# 12-MASELE
# m = int(input("m: "))
# t = m / 1000
# print(f"{m} kilogramm {t} tonnaga ten boladi")

# 13-MASELE
# a = int(input(" Eki xanali sandi kiritin "))
# b = a // 10
# c = a % 10
# print(f"{b} birlikler xanasindagi cifr, {c} onliqlar xanasindagi cifr")

# 14-MASELE
# a = int(input(" Ush xanali sandi kiritin "))
# b = (a // 10) // 10
# c = (a % 10)
# e = (a // 10) % 10
# print(f"{b} birinshi cifr, {e} ekinshi cifr, {c} ushinshi cifr")
# s = b + c + e
# print(f"Ush xanali sannin cifrlari qosindisi {s} ge ten ")

# 15-MASELE
# a = int(input(" a ni kiritin "))
# b = list()
# for san in range(1,a,2):
#     b.append(san)
# print(san)
# print(b)

# a = int(input(" a ni kiritin: "))
# taq_sanlar = list(range(1,a,2))
# print(taq_sanlar)

# 16-MASELE
# a = int(input(" a ni kiritin "))
# b = list()
# for i in range(a+1): # range(start, stop, step)
#     b.append(i ** 2)
# print(b)

# 17-MASELE
# a = int(input(" a ni kiritin "))
# num1 = list()
# num = list(range(a+1))
# num1.append(num.reverse())
# print(num)

# 18-MASELE
# koshe = "ALMAZAR"
# mahalle = "GULZAR"
# rayon = "MOYNAQ"
#print(f"{koshe} koshesi, {mahalle} mahallesi, {rayon} rayoni")

# 19-MASELE
# koshe = str(input("kosheni kiritin"))
# mahalle = str(input("mahalleni kiritin"))
# rayon = str(input("rayondi kiritin"))
# print(f"{koshe} koshesi, {mahalle} mahallesi, {rayon} rayoni")

# 20-MASELE
# koshe = "\nAlmazar"
# mahalle = "\nGulzar"
# rayon = "\nMoynaq"
# print(koshe, "koshesi", mahalle, "mahallesi", rayon, "rayoni")

# 21-MASELE
# address = f"{koshe} koshesi {mahalle} mahallesi {rayon} rayoni"
# print(address)

# 22-MASELE : TITLE
# address = f"\n{koshe} koshesi \n{mahalle} mahallesi \n{rayon} rayoni"
# print(address.title())

# 23-MASELE : UPPER
# address = f"\n{koshe} koshesi \n{mahalle} mahallesi \n{rayon} rayoni"
# print(address.upper())

# 24-MASELE : LOWER
# address = f"\n{koshe} koshesi \n{mahalle} mahallesi \n{rayon} rayoni"
# print(address.lower())

# 25-MASELE : CAPITALIZE
# address = f"\n{koshe} koshesi \n{mahalle} mahallesi \n{rayon} rayoni"
# print(address.capitalize())

# 26-MASELE : Paydanalaniwshi kirgizgen sannin kvadrati ham kubin esaplawshi pogramma
# num = 2
# print(num ** 2)
# print(num ** 3)

# 27-MASELE : Paydanalaniwshi jasin sorap onin tuwilgan kunin jilin esaplawshi programma
# age = int(input(" Jasti kiritin "))
# year = 2003
# print(f"jasim {age} da, {year} jilman")

# 28-MASELE : Paydalaniwshi eki san kirgiziwin sorap kirgizgen sanlardin
# qosindisin, ayirmasin, kobeymesin, tiyindisin shigariwshi programma
# num1 = int(input(" Birinshi sandi kiritin "))
# num2 = int(input(" Ekinshi sandi kiritin "))
# print(num1 + num2) 
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

# 29-MASELE
# import math
# a = int(input("a ni kiritin"))
# p = 4 * a
# print("Perimetri",p)

# 30-MASELE
# import math
# a = int(input("a ni kiritin"))
# s = a * a
# print("Maydani",s)

# 31-MASELE
# names = ["Allambergen"]
# names.pop()
# print(names)

# 32-MASELE
# import math
# a = int(input("a ni kiritin"))
# b = int(input("b ni kiritin"))
# s = a * b
# p = 2 * (a + b)
# print(f"\nMaydani {s} ten \nPerimetri {p} ten ")

# 33-MASELE
# p = 0
# s = 0
# a = int(input(" a ni kiritin "))
# b = int(input(" b ni kiritin "))
# for i in range(a, b):
#     p = p + i**2
# print(p)

# 34-MASELE
# a = int(input(" a ni kiritin "))
# b = int(input(" b ni kiritin "))
# s = 0
# while (a<b):
#     s = s + a ** 2
#     a += 1
# print(s)

# 35-MASELE
# s = 1
# n = int(input(" n di kiritin "))
# for i in range(1, n+1):
#     s = s + 1/i
# print(int(s))

# i = 1
# s = 0
# n = int(input(" n di kiritin "))
# while i < n+1:
#     s += 1/i
#     i += 1
# print(f"qosindisi {s}")
"""

# 36-MASELE
# dostim = {"Dostim": "Atabek", "Tuwilgan jeri": "Xojeli", "Oqiytugin jeri": "QMU"}
# print(dostim)

# 37-MASELE
# dostim = {"Dostim": "Atabek", "Tuwilgan jeri": "Xojeli", "Oqiytugin jeri": "QMU"}
# print(f"Dotimnin ati {dostim['Dostim'].title()}, "
#       f"\n{dostim['Tuwilgan jeri'].title()} de tuwilgan "
#       f"\n{dostim['Oqiytugin jeri'].title()} da oqiydi")

# 38-MASELE
# temalar = {"float": "Haqiyqiy sanlar",
#          "integer": "Putin sanlar",
#          "complex": "Kompleks sanlar",
#           "string": "Qatarli magluwmat",
#             "char": "Simboliq magluwmat",
#           "append": "Listke element qosiw",
#              "len": "Eelementler uzinligin aniqlaw",
#            "range": "Turli araliqtagi sanlar",
#          "if-else": "Shart operatori",
#              "for": "Takirarlaw operatori"}
# print(temalar)

# 39-MASELE
# soz = input(" SOZ: ")
# temalar = {"float": "Haqiyqiy sanlar",
#          "integer": "Putin sanlar",
#          "complex": "Kompleks sanlar",
#           "string": "Qatarli magluwmat",
#             "char": "Simboliq magluwmat",
#           "append": "Listke element qosiw",
#              "len": "Eelementler uzinligin aniqlaw",
#            "range": "Turli araliqtagi sanlar",
#          "if-else": "Shart operatori",
#              "for": "Takirarlaw operatori"}
#
# if soz in temalar:
#     print(temalar[soz])
# else:
#     print("Bunday soz joq")

# 40-MASELE
# soz = input(" SOZ: ")
# temalar = {"float": "Haqiyqiy sanlar",
#          "integer": "Putin sanlar",
#          "complex": "Kompleks sanlar",
#           "string": "Qatarli magluwmat",
#             "char": "Simboliq magluwmat",
#           "append": "Listke element qosiw",
#              "len": "Eelementler uzinligin aniqlaw",
#            "range": "Turli araliqtagi sanlar",
#          "if-else": "Shart operatori",
#              "for": "Takirarlaw operatori"}
#
# print(temalar.get(soz, "Bunday soz joq"))

# 41-MASELE
# myfile = open("input.txt", "w+")
# yyyy = int(input(" A: "))
# if 1 < yyyy < 9999:
#     myfile.write(str(yyyy))
# myfile.close()
# myfile1 = open("output.txt", "w+")
# dd = 12
# mm = 9
# myfile1.write(f"{dd}/{mm}/{yyyy}")
# myfile1.close()

# 42-MASELE
# myfile = open("input.txt", "w+")
# a = int(input(" A: "))
# b = int(input(" B: "))
# c = int(input(" C: "))
# d = int(input(" D: "))
# e = int(input(" E: "))
# myfile.write(f"{a} {b} {c} {d} {e}")
# myfile1 = open("output.txt", "w+")
# myfile1.write(f"maxsinmum = {max(a,b,c,d,e)} ")
# myfile1.write(f"\nminimumi = {min(a,b,c,d,e)} ")
# myfile1.close()

# 43-MASELE
# mylist = [1, 1, 2, 2, 3, 3, 4, 4, 6, 6]
# mylist1 = set(mylist)
# mylist2 = set(mylist1)
# print(mylist2)

# 44-MASELE
# sozler = {"float": "Haqiyqiy sanlar",
#          "integer": "Putin sanlar",
#          "complex": "Kompleks sanlar",
#           "string": "Qatarli magluwmat",
#             "char": "Simboliq magluwmat",
#           "append": "Listke element qosiw",
#              "len": "Eelementler uzinligin aniqlaw",
#            "range": "Turli araliqtagi sanlar",
#          "if-else": "Shart operatori",
#              "for": "Takirarlaw operatori"
#           }
# for key, value in sozler.items():
#     print(f"{key.title()} - {value.title()}")

# 45-MASELE
# country1 = {"Portugaliya": "Lissabon", "Ozbekistan": "Tashkent", "Qaraqalpaqistan": "Nokis",
#            "Rossiya": "Moskva", "Aqsh": "Vashington"}
# for key, value in  country.items():
#     print(f"{key} ")
#     print(f"{value} \n")

# 46-MASELE
# paytaxt = str(input())
# if paytaxt in country1:
#    print(paytaxt)

# 47-MASELE
# onimler = {
#      "alma": 10000,
#      "almurt": 12000,
#      "anar": 13000,
#      "qawin": 14000,
#      "garbiz": 15000,
#      "pomidor": 40000,
#      "geshir": 7000,
#      "baliq": 80000
# }
# a = input()
# b = input()
# c = input()
# print(onimler.get(a, "bunday awqat joq"))
# print(onimler.get(b, "bunday awqat joq"))
# print(onimler.get(c, "bunday awqat joq"))
# for i in range(3):
#     d = input("Awqat: ")
#     print(onimler.get(d, "bunday awqat joq"))

# 48-MASELE
# a = int(input(" A: "))
# b = a % 10
# c = a // 10
# print(f"Onliqlar {b} birlikler {c} ")

# 49-MASELE
# a = int(input(" A: "))
# b = a // 10
# c = a % 10
# print(c*10+b)

# 50-MASELE
# a = int(input(" A: ")) # 123
# b = a // 10 // 10
# c = a // 10 % 10
# d = a % 10
# print(b + c + d)

# 51-MASELE
# a = int(input(" A: "))
# b = a // 10 // 10
# c = a // 10 % 10
# d = a % 100 % 10
# print(d*100 + c*10 + b )

# 52-MASELE
# n = int(input(" N: "))
# M = n/60
# print(M)

# 53-masele
# dost1 = {
#     "surname": "Azizbek",
#     "name": "Qalbaev",
#     "age": 19
# }
#
# dost2 = {
#     "surname": "Duysenbaeva",
#     "name": "Sanemxan",
#     "age": 18
# }
#
# dost3 = {
#     "surname": "Jumanazarova",
#     "name": "Zayfuna",
#     "age": 19
# }
#
# doslarim = [dost1, dost2, dost3]
# for name in doslarim:
#     print(f"{name['surname'].title()} {name['name'].title()} {name['age']} jasta")

# 54-MASELE
# kino = {"Azizbek": ["Goodzilla", "Transformers", "Forsaj"], "Allambergen": ["King Kong", "Bamblbi", "Avatar"],
#         "Sultanbek": ["Naruto", "Madagaskar", "Temir adam"]}
# for key, values in kino.items():
#     print(f" Doslarim {key}")
#     for var in values:
#         print(f"Jaqsi korgen kinolari {var}")

# 55-MASELE
# country = input()
# mamlektler = {
# "Rossiya": ["17100000 km", "Moskva"],
# "Qaraqalpaqsitan": ["166.9 km", "Nokis"],
# "Aqsh": ["9.8 milion kv km", "Vashington"],
# "Portugaliya": ["92,3 ming km", "Lissabon"]
# }
# for var in mamlektler.values():
#     print(f"Mamleketleri haqqinda magluwmat {var}")


# 56-MASELE
# x = int(input(" X: "))
# y = int(input(" Y: "))
# def sannin_dareje(x, y):
#     print(f" X tin y darejesi {x ** y}")
# sannin_dareje(x, y)

# 57-MASELE
# def insan(ati, insan):
#     """PAYDALANIWSHI JILIN ESAPLAWSHI FUNKCIYA"""
#     result = f"{ati.title()} {2023 - jasi} jilda tuwilgan"
#     print(result)
# ati = input(" ATINIZDI KIRITIN: ")
# jasi = int(input())
# insan(ati, jasi)

# 58-MASELE
# san1 = int(input("san1 = "))
# san2 = int(input("san2 = "))
# def sannin_kubi(san1, san2):
#     print(f"Sannin kvadrati {san1 ** 2}")
#     print(f"Sannin kubi {san2 ** 3}")
# sannin_kubi(san1, san2)

# 59-MASELE
# san1 = int(input("san1 = "))
# def jup_ham_taq(san1):
#     if san1%2 == 0:
#         print(f" Jup san {san1}")
#     else:
#         print(f" Taq san {san1}")
#
# jup_ham_taq(san1)

# 60-MASELE
# def araliq(stop, start = 0, step = 1):
#     result = []
#     while start < stop:
#         result.append(start)
#         start += step
#     return result
# print(araliq(10, 5, 2))

# 61-MASELE
# def summa(x, y, *sanlar):
#     a = 1
#     for san in sanlar:
#         a *= san
#     return a

# 62-MASELE
# A = float(input(" A: "))
# B = float(input(" B: "))
# C = float(input(" C: "))
# D = int(input(" D: "))
# E = int(input(" E: "))
# def powerA3(A,B,C,D,E):
#     power1 = f"{A*A*A}"
#     power2 = f"{B*B*B}"
#     power3 = f"{C*C*C}"
#     power4 = f"{D*D*D}"
#     power5 = f"{E*E*E}"
#     return power1, power2, power3, power4, power5
# print(powerA3(A,B,C,D,E))

# 63-MASELE
# A = float(input(" A: "))
# B = float(input(" B: "))
# C = float(input(" C: "))
# def powerA234(A,B,C):
#     dar1 = A*A
#     dar2 = B*B*B
#     dar3 = C*C*C*C
#     return dar1, dar2, dar3
# print(powerA234(A,B,C))

# 64-MASELE
# from math import sqrt
# a = int(input(" A: "))
# b = int(input(" B: "))
# c = int(input(" C: "))
# d = int(input(" D: "))
# def mean1(a, b):
#     oa = (a + b)/2
#     og = sqrt(a * b)
#     return og
#     return oa
# arif = mean1(a, b)
# geo = mean1(a, b)
# print(f"Orta arifmetik {int(arif)}  \nOrta geometrik {int(geo)}")
# def mean2(a, c):
#     oa = (a + c)/2
#     og = sqrt(a * c)
#     return og
#     return oa
# arif = mean2(a, c)
# geo = mean2(a, c)
# print(f"Orta arifmetik {int(arif)}  \nOrta geometrik {int(geo)}")
# def mean3(a, d):
#     oa = (a + d)/2
#     og = sqrt(a * d)
#     return og
#     return oa
# arif = mean3(a, d)
# geo = mean3(a, d)
# print(f"Orta arifmetik {int(arif)}  \nOrta geometrik {int(geo)}")
