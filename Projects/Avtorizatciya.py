from tkinter import messagebox

import customtkinter
from customtkinter import *

window = tkinter.Tk()
window.title('Registratciya')
window.geometry('450x230')
window.resizable(False, False)
window.config(bg="Purple4", border=4)
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 6}
header_padding = {'padx': 10, 'pady': 12}
padding = {'padx': 150, 'pady': 150}
base_padding1 = {'padx': 10, 'pady': 9}
def clicked():

    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Заголовок', '{username}, {password}'.format(username=username, password=password))

main_label = CTkLabel(master=window, text="Registratciya", text_font=font_header, justify=tkinter.CENTER)
main_label.pack(header_padding)

username_label = CTkLabel(master=window, text='Paydalaniwshi Ati',width=150 , text_font=label_font )
username_label.pack(base_padding)

username_entry = CTkEntry(master=window, bg='#fff', fg='#444',width=150 , font=font_entry)
username_entry.pack()

password_label = CTkLabel(master=window, text='Paydalaniwshi Paroli',width=150 , text_font=label_font )
password_label.pack(base_padding)

password_entry = CTkEntry(master=window, bg='#fff', fg='#444',width=150 , font=font_entry)
password_entry.pack()

send_btn = CTkButton(master=window, text='Sign up',fg_color="Purple3",corner_radius=10,height=30, command=clicked)
send_btn.pack(base_padding1)

window.mainloop()