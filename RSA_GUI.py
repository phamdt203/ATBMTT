import tkinter as tk
from tkinter import ttk
import File_method
from tkinter.filedialog import askopenfilename
import datetime
import CreatKey
from MD5_hash import hash
from toBase16 import hex_to_decimal
from docx import Document
from docx2pdf import convert
import PyPDF2
from docxtpl import DocxTemplate
import numpy as np

window = tk.Tk()
window.geometry("1900x1900")
window.title("ATBMTT - Chữ Ký điện tử RSA")

def buttonFileInput():
    fn = askopenfilename()
    try:
        contents = File_method.read_input(fn)
        inp_text_1.delete(1.0, 'end')
        inp_text_1.insert('end', contents)
    except:
        doc = DocxTemplate(fn)
        context = doc.get_context()
        inp_text_1.delete(1.0, 'end')
        for paragraph in context["document"]:
            text = paragraph.text
            inp_text_1.insert('end', text)
                

def buttonSaveInput():
    if len(inp_key_1.get(1.0, 'end')) == 1:
        tk.messagebox.showwarning(title = "ERROR", message = "Vui lòng nhập input để lưu.")
        return()
    fileName = datetime.datetime.now().microsecond
    
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(inp_key_1.get(1.0, 'end'))
            tk.messagebox.showwarning(title = "Ting Ting", message = "Lưu thành công !!!")

def buttonSendKey():
    if len(inp_key_1.get(1.0, 'end')) == 1:
        tk.messagebox.showwarning(title = "ERROR", message = "Vui lòng nhập vào key !")
        return()

    if len(inp_text_1.get(1.0, 'end')) == 1:
        tk.messagebox.showwarning(title = "ERROR", message = "Vui lòng nhập vào văn bản !")
        return()
    
    inp_key_2.delete(1.0, 'end')
    inp_key_2.insert('end', inp_key_1.get(1.0, 'end'))
    inp_text_2.delete(1.0, 'end')
    inp_text_2.insert('end', inp_text_1.get(1.0, 'end'))
    return()

def getKey():
    if q_text.get("1.0", 'end-1c').isdecimal() and p_text.get("1.0", 'end-1c').isdecimal() and b_text.get("1.0", 'end-1c').isdecimal():
        q_read = int(q_text.get("1.0", 'end-1c'))
        p_read = int(p_text.get("1.0", 'end-1c'))
        b_read = int(b_text.get("1.0", 'end-1c'))
        return CreatKey.key_generate(p_read, q_read, b_read)
    else:
        tk.messagebox.showwarning(title = "ERROR", message = "Giá trị p,q,b nhập vào không hợp lệ")
        p_text.delete(1.0, 'end')
        q_text.delete(1.0, 'end')
        b_text.delete(1.0, 'end')

def Sign_Key():
    hash_value = hash(inp_text_1.get(1.0, 'end').strip())[0]
    public_key, private_key = getKey()
    Base_Ten = []
    for i in range(len(hash_value)):
        Base_Ten.append(hex_to_decimal(hash_value[i]))
    signature = '-'.join([str((i**private_key[0]) % public_key[1]) for i in Base_Ten])
    inp_key_1.delete(1.0, 'end')
    inp_key_1.insert('end', signature)

def buttonAutoGenerateKey():
    p = np.random.randint(1000)
    q = np.random.randint(1000)
    b = np.random.randint(1000)
    p_text.delete(1.0, 'end')
    q_text.delete(1.0, 'end')
    b_text.delete(1.0, 'end')
    p_text.insert('end', p)
    q_text.insert('end', q)
    b_text.insert('end', b)

def Check_Key():
    hash_value = hash(inp_text_2.get(1.0, 'end').strip())[0]
    public_key, private_key = getKey()
    Base_Ten = []
    for i in range(len(hash_value)):
        Base_Ten.append(hex_to_decimal(hash_value[i]))
    signature = '-'.join([str((i**private_key[0]) % public_key[1]) for i in Base_Ten])
    if signature == inp_key_2.get(1.0, 'end').strip() : 
        output.delete(1.0, 'end')
        output.insert('end', "Chữ ký đúng")
    else:
        output.delete(1.0, 'end')
        output.insert('end', "Chữ ký sai")

def Clear():
    inp_text_1.delete(1.0, 'end')
    inp_text_2.delete(1.0, 'end')
    inp_key_1.delete(1.0, 'end')
    inp_key_2.delete(1.0, 'end')
    output.delete(1.0, 'end')
    q_text.delete(1.0, 'end')
    p_text.delete(1.0, 'end')
    b_text.delete(1.0, 'end')

def exitApplication():
    window.destroy()

title_1 = tk.Label(window, text = "PHÁT SINH CHỮ KÝ", fg = "black", font = ("Arial", 10), justify= "left")
title_2 = tk.Label(window, text = "KIỂM TRA CHỮ KÝ", fg = "black", font = ("Arial", 10), justify= "left")
text_1 = tk.Label(window, text = "Văn bản ký :", fg = "black", font = ("Arial", 10), justify = "left")
text_2 = tk.Label(window, text = "Văn bản ký :", fg = "black", font = ("Arial", 10), justify = "left")
key_1 = tk.Label(window, text = "Chữ ký :", fg = "black", font = ("Arial", 10), justify = "left")
key_2 = tk.Label(window, text = "Chữ ký :", fg = "black", font = ("Arial", 10), justify = "left")
imform = tk.Label(window, text = "Thông báo :", fg = "black", font = ("Arial", 10), justify = "left")
q_label = tk.Label(window, text = "Nhập q : ", fg = "black", font = ("Arial", 10), justify= "left")
p_label = tk.Label(window, text = "Nhập p : ", fg = "black", font = ("Arial", 10), justify = "left")
b_label = tk.Label(window, text = "Nhập b : ", fg = "black", font = ("Arial", 10), justify = "left")

title_1.place(x = 200, y = 20)
title_2.place(x = 1100, y = 20)
text_1.place(x = 20, y = 100)
text_2.place(x = 900, y = 100)
key_1.place(x = 20, y = 500)
key_2.place(x = 900, y = 380)
imform.place(x = 800, y = 500)
q_label.place(x = 20, y = 230)
p_label.place(x = 220, y = 230)
b_label.place(x = 420, y = 230)

inp_text_1 = tk.Text(window, width = 60, height = 5)
inp_text_2 = tk.Text(window, width = 60, height = 5)
inp_key_1 = tk.Text(window, width = 60, height = 5)
inp_key_2 = tk.Text(window, width = 60, height = 5)
output = tk.Text(window, width = 60, height = 5)
q_text = tk.Text(window, width = 15, height= 2)
p_text = tk.Text(window, width = 15, height= 2)
b_text = tk.Text(window, width = 15, height= 2)

inp_text_1.place(x = 20, y = 120)
inp_text_2.place(x = 900, y = 120)
inp_key_1.place(x = 20, y = 520)
inp_key_2.place(x = 900, y = 400)
output.place(x = 900, y = 600)
q_text.place(x = 105 - 30, y = 230)
p_text.place(x = 305 - 30, y = 230)
b_text.place(x = 505 - 30, y = 230)

buttonFileInput_1 = tk.Button(window, text = "File", command = buttonFileInput, cursor = "hand2", width = 15, height = 5, bg = "white")
buttonFileInput_1.place(x = 550, y = 120)

buttonGenerateKey = tk.Button(window, text = "Random key", command = buttonAutoGenerateKey, cursor = "hand2", width = 10, height = 3, bg = "white")
buttonGenerateKey.place(x = 650, y = 230)

Sign = tk.Button(window, text = "Kí", command = Sign_Key, cursor = "hand2", width = 15, height= 5, bg = "white")
Sign.place(x = 200, y = 330)

Transmit = tk.Button(window, text = "Chuyển", command = buttonSendKey, cursor = "hand2", width= 15, height = 5, bg = "white")
Transmit.place(x = 550, y = 500)

Save = tk.Button(window, text = "Lưu", command = buttonSaveInput, cursor = "hand2", width= 15, height = 5, bg = "white")
Save.place(x = 550, y = 600)

buttonFileInput_2 = tk.Button(window, text = "File văn bản", command = buttonFileInput, cursor = "hand2", width = 15, height = 5, bg = "white")
buttonFileInput_2.place(x = 1400, y = 120)

keyFile = tk.Button(window, text = "File chữ kí", command = buttonFileInput, cursor = "hand2", width = 15, height = 5, bg = "white")
keyFile.place(x = 1400, y = 400)

Check = tk.Button(window, text = "Kiểm tra chữ kí", command = Check_Key, cursor = "hand2", width= 15, height = 5, bg = "white")
Check.place(x = 1100, y = 500)

Clear = tk.Button(window, text = "Xoa", command = Clear , cursor = "hand2", width = 5, height = 3, bg = "white")
Clear.place(x = 1450, y = 650)

exit_application = tk.Button(window, text = "Thoát", command = exitApplication, cursor = "hand2", width = 5, height = 3, bg = "white")
exit_application.place(x = 1550, y = 650)

window.mainloop()