"""DICTIONARY"""

# keyboard = value
# car_0 = {"model": "ferari", "color": "qizil"}
# print(car_0)

"""DICTIONARY MENEN ISLEW"""

# car_0 = {"model": "ferrari", "color": "qizil"}
# print(car_0['model'])
# print(car_0['color'])

# """dicke int, float, string, list, tuple, ham dicting ozinde saqlawga boladi"""
# student_0 = {"name": "Azizbek", "age": "19", "birth": "2003"}
# print(f"{student_0['name'].title()}, \
# {student_0['birth'].title()} - jilda tuwilgan, \
# {student_0['age']} jasta")

"""TAZA JUPLIQ QOSIW"""

# student_0['Baxasi'] = 4
# student_0['Fakulteti'] = 'Matematika'
# print(student_0)

"""BOS DICTIONARY"""

# student_1 = {}
# student_2 = {}
# student_1['Name'] = "Duysenbaeva Sanemxan"
# student_1['Tuwilgan jeri'] = "\nNokis qalasi"
# student_1['Tuwilgan datasi'] = "07.13.2004"
# student_1["Oqiytugin jeri"] = "QMU"
# student_1["Fakulteti"] = "Matematika"
# student_1["Gruppasi"] = "2v3"
# student_2["name"] = "Qalbaev Azizbek"
# print(f"Student - {student_1['Name'].title()}, {student_1['Tuwilgan jeri'].title()} da, \
# \n{student_1['Tuwilgan datasi'].title()}, tuwilgan  \n{student_1['Oqiytugin jeri'].title()} da oqiydi \
# \n{student_1['Fakulteti'].title()} da oqiydi \n{student_1['Gruppasi'].title()}-gruppasi")
#
#
# n = int(input(" n di kiritin "))
# person = {}
# for i in range(n):
#     gilt = input("Keyword")
#     manis = input("Value")
#     person[gilt] = manis
# print(person)

"""MANISTI OZGERTIW"""

# student_1['kurs'] = 2
# print(f"{student_1['Name'].title()} Dauranbekovna \n{student_2['name'].title()} Marqabaevich")

"""GILT SOZ-MANIS JUPLIGIN OSHIRIW"""

# student_0 = {"name": "Sanem", "age": "18", "birth": "2004"}
# print(student_0)
# del student_0['age']
# print(student_0)

"""DICTIONARY QATARGA BOLIP JAZIW"""

# Sanemxannin_doslari = {"1-dostim": "Zayfuna", "2-dostim": "Venera", "3-dostim": "Gulzar"}
# print(Sanemxannin_doslari)

"""GET() METODI"""

# doslar = Sanemxannin_doslari["1-dostim"]
# print(f"Sanemxannnin podrushkasi bul {doslar.title()}")
#
# doslar = Sanemxannin_doslari["2-dostim"]
# print(f"Sanemxannnin podrushkasi bul {doslar}")
#
# doslar = Sanemxannin_doslari.get("Aloo", "Magluwmat joq")
# print(doslar)
#
# magluwmat = f"1 shi Dostimnin ati {Sanemxannin_doslari['1-dostim'].title()}"
# magluwmat += f"\n2 shi Dostimnin ati {Sanemxannin_doslari['2-dostim'].title()}"
# magluwmat += f"\n3-shi Dostimnin ati {Sanemxannin_doslari['3-dostim'].title()}"
# print(magluwmat)

"""DICTIONARY MENEN ISLEW"""

""".items() METODI"""
"""BUL METOD ARQALI DICT ISHINDEGI BARSHE KEY-VALUE JUPLIQLARDI KORIW MUMKIN"""

# student = {
#     "full-name": "Elbrus Sarsenbaev",
#     "year_of_birth": 2000,
#     "age": 23, "faculty": "matematika",
# "level": 4 }
# print(student.items())
#
# """for ham items()"""
# for key, value in student.items():
#     print(f"Key: {key}")
#     print(f"Value: {value} \n")

telefonlar = {"ali": "iphone x",
              "abiw": "galaxy s9",
              "wali": "mi 9 pro",
              "gani": "nokia 310",
              "sanem": "Redmi note 7",
              "atabek": "galaxy a10",
              "azizbek": "galaxy j7"}
# for k, q in telefonlar.items():
#     print(f"{k.title()} din telefoni {q.title()}")

""" .keys() METODI"""
# # Eger dictegi giltsozler dizimi bolsa paydalanamiz
# onimler = {
#     "alma": 10000,
#     "almurt": 12000,
#     "anar": 13000,
#     "qawin": 14000,
#     "garbiz": 15000,
#     "pomidor": 40000,
#     "geshir": 7000,
#     "baliq": 80000
# }
# print(f"{onimler.keys()} usi zatlar bazarda satiladi")
#
# print("Dukandagi onimler: ")
# for onim in onimler.keys():
#     print({onim.title()})
#
# bazarliq = ["alma", "almurt", "garbiz", "qawin", "gosh", "gril", "erik"]
# for onim in onimler:
#     if onim in bazarliq:
#         print(f"{onim.title()} {onimler[onim]}")

# for narse in bazarliq:
#     if narse not in onimler:
#         print(f"Otinish {narse} alip kelin...")

"""DICT ELEMENTLERIN TARTIP  PENEN SHIGARIW"""
# print("Duknadagi onimler")
# for onim in sorted(onimler, reverse=True):
#     print(onim.title())

""".values() METODI """
# telefonlar = {"ali": "iphone x",
#               "abiw": "galaxy s9",
#               "wali": "mi 9 pro",
#               "gani": "nokia 310"}
# print(f"Olardin telefonlari {telefonlar.values()}")

# print("Paydalaniwshilar tomendegishe telefonlardan paydalaniladi")
# for telefon in telefonlar.values():
#     print(telefon)
#
# for telefon in set(telefonlar.values()):
#     print(telefon)

"""TYPECASTING"""
# a = input(" A: ")
# print(type(a))
# name = "JHON"
# age = 26
# message = name + " "  + str(age) + " " + "jasta"
# print(message)

# LIST()
# set()
