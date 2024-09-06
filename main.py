from tkinter import *
import tkinter as tk
import PIL
from PIL import ImageTk, Image
import PIL.Image
import os
from pygame import mixer
import open_keys
import open_marketing


import open_pestel
import open_test


import sys

def resource_path(relative_path):
    """ PyInstaller uchun resurs yo'lini topish """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Elektron darslik")
image_path = resource_path('Images/images (4).jpg')
icon_img = ImageTk.PhotoImage(PIL.Image.open(image_path))
root.wm_iconphoto(False, icon_img)


    

    
image_path_1 = resource_path('Images/img1.jpg')

img_1 = ImageTk.PhotoImage(PIL.Image.open(image_path_1).resize((800,600)))

def home_page():
    canvas = tk.Canvas(main_frame, width=800, height=600)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img_1)
    btn_1 = tk.Button(main_frame, text='Keys study', bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda: new_frame(key_stadi_page))
    btn_1.place(x=50, y=100)
    btn_2 = tk.Button(main_frame, text="Marketing amaliy mashg'ulotlar", bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda:new_frame(marketing_page))
    btn_2.place(x=50, y=200)
    btn_3 = tk.Button(main_frame, text="Mustaqil ta'lim", bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda:new_frame(mustaqil_page) )
    btn_3.place(x=50, y=300)
    btn_4 = tk.Button(main_frame, text="Pest tahlillar", bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda:new_frame(pestel_page) )
    btn_4.place(x=550, y=100)
    btn_5 = tk.Button(main_frame, text="Savollar", bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda:new_frame(question_page) )
    btn_5.place(x=550, y=200)
    btn_6 = tk.Button(main_frame, text="Test", bg='#A3E4D7', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda:new_frame(test_page) )
    btn_6.place(x=550, y=300)
    btn_7 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda: new_frame(new_page))
    btn_7.place(x=640, y=525)

image_path_2 = resource_path('Images/img2.webp')
img2 = ImageTk.PhotoImage(PIL.Image.open(image_path_2).resize((450,600)))
  
def key_stadi_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#D0ECE7')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img2)
    btn_1 = tk.Button(main_frame, text='1 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k1())
    btn_1.place(x=470, y=50)
    btn_2 = tk.Button(main_frame, text='2 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k2())
    btn_2.place(x=570, y=50)
    btn_3 = tk.Button(main_frame, text='3 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k3())
    btn_3.place(x=670, y=50)
    btn_4 = tk.Button(main_frame, text='4 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k4())
    btn_4.place(x=470, y=120)
    btn_5 = tk.Button(main_frame, text='5 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k5())
    btn_5.place(x=570, y=120)
    btn_6 = tk.Button(main_frame, text='6 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k6())
    btn_6.place(x=670, y=120)
    btn_7 = tk.Button(main_frame, text='7 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k7())
    btn_7.place(x=470, y=190)
    btn_8 = tk.Button(main_frame, text='8 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k8())
    btn_8.place(x=570, y=190)
    btn_9 = tk.Button(main_frame, text='9 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k9())
    btn_9.place(x=670, y=190)
    btn_10 = tk.Button(main_frame, text='10 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k10())
    btn_10.place(x=470, y=260)
    btn_11 = tk.Button(main_frame, text='11 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k11())
    btn_11.place(x=580, y=260)
    btn_12 = tk.Button(main_frame, text='12 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k12())
    btn_12.place(x=690, y=260)
    btn_13 = tk.Button(main_frame, text='13 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k13())
    btn_13.place(x=470, y=330)
    btn_14 = tk.Button(main_frame, text='14 - dars', bg='#85C1E9', font=('Helvetica 15 bold'), bd=1, fg='black', command=lambda : open_keys.open_file_k14())
    btn_14.place(x=580, y=330)
    btn_15 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_15.place(x=650, y=525)

image_path_3 = resource_path('Images/img3.jpg')
img3 = ImageTk.PhotoImage(PIL.Image.open(image_path_3).resize((800,600)))

def marketing_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#3498DB')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img3)
    btn_1 = tk.Button(main_frame, text='1 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m1())
    btn_1.place(x=470, y=150)
    btn_2 = tk.Button(main_frame, text='2 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m2())
    btn_2.place(x=560, y=150)
    btn_3 = tk.Button(main_frame, text='3 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m3())
    btn_3.place(x=650, y=150)
    btn_4 = tk.Button(main_frame, text='4 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m4())
    btn_4.place(x=470, y=200)
    btn_5 = tk.Button(main_frame, text='5 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m5())
    btn_5.place(x=560, y=200)
    btn_6 = tk.Button(main_frame, text='6 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m6())
    btn_6.place(x=650, y=200)
    btn_7 = tk.Button(main_frame, text='7 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m7())
    btn_7.place(x=470, y=250)
    btn_8 = tk.Button(main_frame, text='8 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m8())
    btn_8.place(x=560, y=250)
    btn_9 = tk.Button(main_frame, text='9 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m9())
    btn_9.place(x=650, y=250)
    btn_10 = tk.Button(main_frame, text='10 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m10())
    btn_10.place(x=470, y=300)
    btn_11 = tk.Button(main_frame, text='11 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m11())
    btn_11.place(x=570, y=300)
    btn_12 = tk.Button(main_frame, text='12 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m12())
    btn_12.place(x=670, y=300)
    btn_13 = tk.Button(main_frame, text='13 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m13())
    btn_13.place(x=470, y=350)
    btn_14 = tk.Button(main_frame, text='14 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m14())
    btn_14.place(x=570, y=350)
    btn_15 = tk.Button(main_frame, text='15 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m15())
    btn_15.place(x=670, y=350)
    btn_16 = tk.Button(main_frame, text='16 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m16())
    btn_16.place(x=470, y=400)
    btn_17 = tk.Button(main_frame, text='17 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m17())
    btn_17.place(x=570, y=400)
    btn_18 = tk.Button(main_frame, text='18 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m18())
    btn_18.place(x=670, y=400)
    btn_19 = tk.Button(main_frame, text='19 - dars', bg='#D0D3D4', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_marketing.open_file_m19())
    btn_19.place(x=470, y=450)
    btn_20 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_20.place(x=650, y=525)  

image_path_4 = resource_path('Images/img4.jpg')
      
img4 = ImageTk.PhotoImage(PIL.Image.open(image_path_4).resize((450,600)))

def pestel_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#A6ACAF')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img4)
    btn_1 = tk.Button(main_frame, text='1 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w1())
    btn_1.place(x=470, y=50)
    btn_2 = tk.Button(main_frame, text='2 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w2())
    btn_2.place(x=560, y=50)
    btn_3 = tk.Button(main_frame, text='3 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w3())
    btn_3.place(x=650, y=50)
    btn_4 = tk.Button(main_frame, text='4 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w4())
    btn_4.place(x=470, y=100)
    btn_5 = tk.Button(main_frame, text='5 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w5())
    btn_5.place(x=560, y=100)
    btn_6 = tk.Button(main_frame, text='6 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w6())
    btn_6.place(x=650, y=100)
    btn_7 = tk.Button(main_frame, text='7 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w7())
    btn_7.place(x=470, y=150)
    btn_8 = tk.Button(main_frame, text='8 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w8())
    btn_8.place(x=560, y=150)
    btn_9 = tk.Button(main_frame, text='9 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w9())
    btn_9.place(x=650, y=150)
    btn_10 = tk.Button(main_frame, text='10 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w10())
    btn_10.place(x=470, y=200)
    btn_11 = tk.Button(main_frame, text='11 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w11())
    btn_11.place(x=570, y=200)
    btn_12 = tk.Button(main_frame, text='12 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w12())
    btn_12.place(x=670, y=200)
    btn_13 = tk.Button(main_frame, text='13 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w13())
    btn_13.place(x=470, y=250)
    btn_14 = tk.Button(main_frame, text='14 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w14())
    btn_14.place(x=570, y=250)
    btn_15 = tk.Button(main_frame, text='15 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w15())
    btn_15.place(x=670, y=250)
    btn_16 = tk.Button(main_frame, text='16 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w16())
    btn_16.place(x=470, y=300)
    btn_17 = tk.Button(main_frame, text='17 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w17())
    btn_17.place(x=570, y=300)
    btn_18 = tk.Button(main_frame, text='18 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w18())
    btn_18.place(x=670, y=300)
    btn_19 = tk.Button(main_frame, text='19 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w19())
    btn_19.place(x=470, y=350)
    btn_20 = tk.Button(main_frame, text='20 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w20())
    btn_20.place(x=570, y=350)
    btn_21 = tk.Button(main_frame, text='21 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w21())
    btn_21.place(x=670, y=350)
    btn_22 = tk.Button(main_frame, text='22 - dars', bg='#D6DBDF', font=('Helvetica 14 bold'), bd=1, fg='black', command=lambda : open_pestel.open_file_w22())
    btn_22.place(x=570, y=400)
    btn_23 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_23.place(x=650, y=525)    

image_path_5 = resource_path('Images/img5.jpg')    
img5 = ImageTk.PhotoImage(PIL.Image.open(image_path_5).resize((800,600)))

def question_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#A6ACAF')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img5)
    btn_1 = tk.Button(main_frame, text='Savollar', bg='#D6EAF8', font=('Helvetica 30 bold'), bd=1, fg='black', command=lambda : open_test.open_file_s1())
    btn_1.place(x=50, y=130)
    btn_23 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_23.place(x=650, y=525)    

image_path_6 = resource_path('Images/img6.jpg')    
img6 = ImageTk.PhotoImage(PIL.Image.open(image_path_6).resize((800,600)))
    
def test_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#A6ACAF')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img6)
    btn_1 = tk.Button(main_frame, text='Test', bg='#D6EAF8', font=('Helvetica 30 bold'), bd=1, fg='black', command=lambda : open_test.open_file_t1())
    btn_1.place(x=50, y=130)
    btn_23 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_23.place(x=650, y=525)   

image_path_7 = resource_path('Images/7.jpg')    
img7 = ImageTk.PhotoImage(PIL.Image.open(image_path_7).resize((800,600)))
    
def mustaqil_page():
    canvas = tk.Canvas(main_frame, width=800, height=600, bg='#A6ACAF')
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW,  image=img7)
    btn_1 = tk.Button(main_frame, text='Mustaqil 1', bg='#D6EAF8', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : open_test.open_file_m1())
    btn_1.place(x=50, y=130)
    btn_2 = tk.Button(main_frame, text='Mustaqil 2', bg='#D6EAF8', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : open_test.open_file_m2())
    btn_2.place(x=50, y=200)
    btn_23 = tk.Button(main_frame, text='Ortga', bg='#D7DBDD', font=('Helvetica 20 bold'), bd=1, fg='black', command=lambda : new_frame(home_page))
    btn_23.place(x=650, y=525)   

def new_page():
    canvas = tk.Canvas(main_frame, bg='#EDBB99', width=800, height=600)
    canvas.create_image(0, 0, anchor=NW, image=main_img)
    canvas.create_text(600, 150, text="Marketing\nfanidan elektron\ndarslik", fill="#2C3E50", font=('Arial 30 bold'))
    canvas.create_text(600, 350, text="Karimova Maftuna", fill="#E74C3C", font=('Arial 25 bold'))
    btn = tk.Button(canvas, text="Boshlash",  bg='#FDEBD0', font=('Helvetica 20 bold'), bd=1, fg='black', command = lambda : new_frame(home_page))
    btn.place(x=600, y=500)
    canvas.pack()
        


def destroy_frame():
    for frame in main_frame.winfo_children():
        frame.destroy()
    
def new_frame(fr):
    destroy_frame()
    fr()

main_frame = tk.Frame(root,height=600, width=800)
image_path_8 = resource_path('Images/images6.jpg')

main_img = ImageTk.PhotoImage(PIL.Image.open(image_path_8).resize((400, 600)))

canvas = tk.Canvas(main_frame, bg='#EDBB99', width=800, height=600)
canvas.create_image(0, 0, anchor=NW, image=main_img)

canvas.create_text(600, 150, text="Marketing\nfanidan elektron\ndarslik", fill="#2C3E50", font=('Arial 30 bold'))
canvas.create_text(600, 350, text="Karimova Maftuna", fill="#E74C3C", font=('Arial 25 bold'))

btn = tk.Button(canvas, text="Boshlash",  bg='#FDEBD0', font=('Helvetica 20 bold'), bd=1, fg='black', command = lambda : new_frame(home_page))
btn.place(x=600, y=500)

canvas.pack()
main_frame.pack()

root.mainloop()