"""Qateler menen islew"""


"""Syntax error"""
# print("Hello world")

"""EOL (End of line - qatar juwmagi)"""
# print("Hello world"

"""EOL (End of function - funkciya juwmagi)"""
#  print("Hello world"

"""Identation error"""
#    print("Hello world")

"""RUN TIME ERROR"""

"""TYPE ERROR"""
# prit("Hello world")

"""ValueError"""
# san = int(input(" Sandi kiritin: "))
# print(f"{san} sannin kvadrati {san**2} ga ten")

"""IndexError"""
# miyweler = ['alma', 'anar', 'banan']
# print(miyweler[3])

"""NameError"""
# name = "Aziz"
# print(nam1)

"""TRY EXCEPT"""
# jas = input(" Jasti kiritin: ")
# jas = int(jas)
# print(f"{2023-jas}-jilda tuwilgansiz.")

# jas = input(" Jasti kiritin: ")
# try:
#     jas = int(jas)
#     print(f"{2023-jas}-jilda tuwilgansiz")
# except:
#     print(f"Putin san kirgizbegensiz")

"""TRY EXPECT-ELSE"""
# jas = int(input(" jasinizdi kiritin: "))
# try:
#     jas = int(jas)
# except:
#     print(f"Putin sandi kirgizbegensiz")
# else:
#     print(f"{2023-jas}-jilda tuwilgansiz")

# print(" Programma juwmaqlandi! ")

"""IndexError"""
# miyweler = ['alma', 'anar', 'almurt']
# try:
#     print(miyweler[7])
# except IndexError:
#     print(f"Listte {len(miyweler)} dana miyweler bar.")


# """KeyError"""
# user = {
#     'username': 'jhon',
#     'email': 'jhon777gmail.com',
#     'phone': '949185020'
# }

# try:
#     print(f"Paydalaniwshi: {user['telefon']}")
# except KeyError:
#     print(f"Bunday gilt soz joq.")


"""TRY EXCEPT-ELSE FINALLY"""
# jas = input("Jasinizdi kiritin - ")
# try:
#     jas = int(jas)
# except:
#     print("Putin sandi kirgizbegensiz")
# else:
#     print(f"{2023-jas}-jilda tuwilgansiz")
# finally:
#     print("Programma juwmaqlandi")

"""BIRNESHE QATELIKLERDI USLAW"""
# n = input("Putin san kiritin: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print(" Putin san kirgizilmegen")        
# except ZeroDivisionError:
#     print("O ge boliwge bolmaydi")
# else: 
#     print(f"x = {x}")


"""QATENIN ALDIN ALIW"""
# jas = input(" Jasinizdi kiritin ")
# if jas.isdigit():
#     jas = int(jas)
#     print(f"{2023-jas}-jilda tuwilgansiz")
# else:
#     print("Putin san kirgizbegensiz")

"""QATELIKLERDI JARATIW"""
# n = int(input("Sandi kiritin"))
# if n == 0:
#     raise ZeroDivisionError("Sandi o ge boliwge bolmaydi")
# else:
#     print(20/n)

"""CASE OPERATORI"""
# color = "sari"
# match color:
#     case 'blue':
#         print("kok")
#     case 'red':
#         print('qizil')
#     case 'black':
#         print('qara')
#     case 'orange':
#         print('geshir')
#     case 'yellow':
#         print('sari')

