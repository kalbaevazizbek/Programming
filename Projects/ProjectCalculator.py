# from tkinter import *
#
# number = ""
#
# root = Tk()
# frame = Frame(root,
#               bg="Black",
#               highlightcolor="Black",
#               highlightbackground="Black",
#               borderwidth=10,
#               relief="solid")
# frame.pack()
# root.geometry("290x360")
# equation = StringVar()
# root.title("CalculatorApp")
# root.resizable(0, 0)
# number_field = Entry(root,
#                      bg="Purple",
#                      borderwidth=9,
#                      highlightthickness=9,
#                      width=46,
#                      textvariable=equation)
# number_field.pack(side=TOP, ipady=24, anchor=W)
#
# def button_clicked(num):
#     global number
#     number = number + str(num)
#     equation.set(number)
#
# def equalpress():
#     try:
#         global number
#         total = str(eval(number))
#         equation.set(total)
#         number = ""
#     except:
#         equation.set("Error")
#         number = ""
#
# def clear():
#     number = ""
#     equation.set("")
#
# font1 = ("Consolas",9)
#
# btn1 = Button(root, text="1",command=lambda :button_clicked(1), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn1.place(x=10, y=100)
#
# btn2 = Button(root, text="2",command=lambda :button_clicked(2), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn2.place(x=80, y=100)
#
# btn3 = Button(root, text="3",command=lambda :button_clicked(3), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn3.place(x=150, y=100)
#
# btn4 = Button(root, text="4",command=lambda :button_clicked(4), font=font1,borderwidth=10, width=5, height=2, bg="Purple")
# btn4.place(x=220, y=100)
#
# btn5 = Button(root, text="5",command=lambda :button_clicked(5), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn5.place(x=80, y=165)
#
# btn6 = Button(root, text="4",command=lambda :button_clicked(4), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn6.place(x=10, y=165)
#
# btn7 = Button(root, text="5",command=lambda :button_clicked(5), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn7.place(x=80, y=165)
#
# btn8 = Button(root, text="6",command=lambda :button_clicked(6), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn8.place(x=150, y=165)
#
# btn9 = Button(root, text="+",command=lambda :button_clicked("+"), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn9.place(x=220, y=165)
#
# btn10 = Button(root, text="7",command=lambda :button_clicked(7), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn10.place(x=10, y=230)
#
# btn11 = Button(root, text="3",command=lambda :button_clicked(3), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn11.place(x=150, y=100)
#
# btn12 = Button(root, text="CE",command=lambda :clear(), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn12.place(x=220, y=100)
#
# btn13 = Button(root, text="0",command=lambda :button_clicked(0), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn13.place(x=10, y=295)
#
# btn14 = Button(root, text="*",command=lambda :button_clicked("*"), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn14.place(x=80, y=295)
#
# btn15 = Button(root, text="8",command=lambda :button_clicked("8"), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn15.place(x=80, y=230)
#
# btn16 = Button(root, text="-",command=lambda :button_clicked("-"), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn16.place(x=220, y=230)
#
# btn17 = Button(root, text="=",command=lambda :equalpress(), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn17.place(x=220, y=295)
#
# btn18 = Button(root, text="/",command=lambda :button_clicked("/"), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn18.place(x=150, y=295)
#
# btn19 = Button(root, text="9",command=lambda :button_clicked(9), font=font1, borderwidth=10, width=5, height=2, bg="Purple")
# btn19.place(x=150, y=230)
#
# root.mainloop()
