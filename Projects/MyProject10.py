# """
# 15.02 - NESTING
# """
#
# # student_0 = {
# #     'name':'Jhon',
# #     'age':20,
# #     'from':'canada'
# # }
#
# # student_1 = {
# #     'name':'Mike',
# #     'age':21,
# #     'from':'portugal'
# # }
#
# # student_2 = {
# #     'name':'Luis',
# #     'age':19,
# #     'from':'poland'
# # }
#
# # student = student_0
# # print(f"{student['name'].title()}, \
# #     {student['age']} jasta, \
# #     {student['from'].title()}")
#
# # student = student_1
# # print(f"{student['name'].title()}, \
# #     {student['age']} jasta, \
# #     {student['from'].title()}")
#
# # student = student_2
# # print(f"{student['name'].title()}, \
# #     {student['age']} jasta, \
# #     {student['from'].title()}")
#
#
# """HAMME MAGLIWMATLARDI BIR LISTKE JIYNAYMIZ"""
# # students = [student_0, student_1, student_2]
# # for student in students:
# #     print(f"{student['name'].title()}, \
# #     {student['age']} jasta, \
# #     {student['from'].title()}")
#
#
# # print(students[0])
# # print(students[0]['name'])
#
#
# """DICT ISHINDE LIST"""
# # programmers = {
# #     'abiw':['python', 'rust'],
# #     'ali':['html', 'css', 'js'],
# #     'wali':['go', 'php'],
# #     'gani':['dart', 'ruby'],
# #     'guli':['c++', 'c#'],
# # }
#
# # for name, langs in programmers.items():
# #     print(f"{name.title()} tomendegi tillerdi biledi:")
# #     for lang in langs:
# #         print(lang.upper())
#
# # for name, langs in programmers.items():
# #     print(f"{name.title()} tomendegi tillerdi biledi:", end=' ')
# #     for lang in langs:
# #         print(lang.upper(), end=' ')
# #     print()
#
# """DICT ISHINDE DICT"""
# # students = {
# #     'abiw':{
# #         'l_name':'asetov',
# #         'birth':2000,
# #         'langs':['python', 'php']
# #     },
# #     'ali':{
# #         'l_name':'bekimbetov',
# #         'birth':1990,
# #         'langs':['c++', 'c#'],
# #     },
# #     'wali':{
# #         'l_name':'saliev',
# #         'birth':2002,
# #         'langs':['java', 'kotlin']
# #     }
# # }
#
# # for name, info in students.items():
# #     message = f"{name.title()} {info['l_name'].title()}, "
# #     message += f"{info['birth']}-jilda tuwilgan. \n"
# #     message += "Tomendegi tillerdi biledi:"
# #     print(message)
# #     for lang in info['langs']:
# #         print(lang.upper(), end=' ')
# #     print("\n")
#
#
# """AMELIYAT"""
# """
# 1-masele:
# 4 taniqli insan haqqinda magliwmatlardi
# dict korinisnde saqlan.
# Dictlerdi bir listke jiynan, ham har bir
# insan haqqindagi magliwmatlardi konsolge shigarin
# """
# person_1 = {
#     'name': 'Ibrayim',
#     "l_name": 'Yusupov',
#     'birth': 1929,
#     'region': 'Shimbay',
#     'shigarmalari': [
#         'Joldas mugallim',
#         'Tumaris',
#         'Jeti asirim'
#     ]
# }
# person_2 = {
#     'name': 'Tolepbergen',
#     'l_name': 'Qayipbergenov',
#     'birth': 1929,
#     'region': 'Kegeyli',
#     'shigarmalari': [
#         'Tilegim',
#         'Pochtalon kelgende',
#         'Sekratar'
#     ]
# }
# person_3 = {
#     'name': 'Berdaq',
#     'l_name': 'Gargabay uli',
#     'birth': 1827,
#     'region': 'Moynaq',
#     'shigarmalari': [
#         'Omirim',
#         'Ernazarbiy',
#         'Jaqsiraq'
#     ]
# }
# person_4 = {
#     'name': 'Kunxoja',
#     'l_name': 'Ibratim uli',
#     'birth': 1799,
#     'region': 'Bozataw',
#     'shigarmalari': [
#         'Jarimadim',
#         'Jaylawim',
#         'Tuye ekensen'
#     ]
# }
# # famous_persons = [person_1, person_2, person_3, person_4]
# # for person in famous_persons:
# #     print(f"{person['name']} {person['l_name']}, {person['birth']}-jilda {person['region']} da tuwilgan.")
# #     print('Tomendegi shigarmalardi jazgan:')
# #     for i in person['shigarmalari']:
# #         print(f'"{i}"', end=', ')
# #     print()
#
#
# """"
# 2-masele:
# Doslardin 3 dana jaqsi korgen kino-seriallarin
# saqlaw ushin dict jaratin.
# Dostinizdin ati key, onin jaqsi korgen
# kinolarin list korinisinde value qilip saqlan.
# Natijeni konsolge shigarin.
# """
# doslarim = {
#     'abiw': [
#         'Qasqirlar makani',
#         'Summerky',
#         'Spider-Man'
#     ],
#     'ali': [
#         'I am Groot',
#         'IronMan',
#         'Tor'
#     ],
#     'wali': [
#         'Hello Mumbai',
#         'Taxi',
#         'Wednesday'
#     ]
# }
# # for name, movies in doslarim.items():
# #     print(f"{name.title()}", end=' ')
# #     for movie in movies:
# #         print(movie, end=', ')
# #     print('kino ham seriallarin jaqsi koredi.')
#
#
# """
# 3-masele:
# mamleketler degen dict jaratin, dict ishine
# bir neshe mamleketler haqqinda magliwmatlardi
# dict korinisinde saqlan.
# Har bir mamleket haqqindagi magliwmatlardi
# konsolge shigarin.
# """
# mamleketler = {
#     'uzbekistan': {
#         'capital': 'Tashkent',
#         'lang': ['uzbek', 'karakalpak', 'turkmen', 'arabic', 'azerbaijan'],
#         'currency': 'sum',
#         'population': 36_407_000,
#         'total_area': 448_978
#     },
#     'kazakhstan': {
#         'capital': 'Nursultan',
#         'lang': ['kazak', 'russian'],
#         'currancy': 'tenge',
#         'population': 19_398_331,
#         'total_area': 2_724_900
#     },
#     'russia': {
#         'capital': 'Moscow',
#         'lang': ['russian', 'tatar', 'bashkir', 'chechen'],
#         'currancy': 'rubl',
#         'population': 147_182_123,
#         'total_area': 17_098_246
#     }
# }
# # for name, info in mamleketler.items():
# #     data = f'{name.title()} '
# #     data += f"paytaxti {info['capital']}, "
# #     data += f"{info['population']} xaliq saninia iye. "
# #     data += "Mamlekette "
# #     for i in info['lang']:
# #         data += i + " "
# #     data += " tillerinde soylesiledi. \n"
# #     data += f"Toliq jer maydani {info['total_area']} km/kv."
# #     print(data)
#
#
# """
# 4-masele:
# Paydalaniwshidan mamleket atin kiritiwdi
# soran ham joqardagi "mamleketler" ishinen
# sol mamleket haqqindagi magliwmatti alip berin.
# Eger joq bolsa "Magliwmat joq" tekstin
# konsolge shigarip berin.
# """
# c_name = input("Mamleket atin kirgizin: ")
# if c_name.lower() in mamleketler:
#     info = mamleketler[c_name.lower()]
#     data = f'{c_name.title()} '
#     data += f"paytaxti {info['capital']}, "
#     data += f"{info['population']} xaliq saninia iye. "
#     data += "Mamlekette "
#     for i in info['lang']:
#         data += i + " "
#     data += " tillerinde soylesiledi. \n"
#     data += f"Toliq jer maydani {info['total_area']} km/kv."
#     print(data)
# else:
#     print('Magliwmat joq')

