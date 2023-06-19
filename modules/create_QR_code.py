import qrcode 
import os
from tkinter import colorchooser, Listbox
from PIL import Image, ImageTk, ImageDraw
import modules.create_entry as m_entry
import customtkinter as ctk
import modules.create_app as m_app
import modules.create_font as m_font
from qrcode import constants
import re

import cv2
import numpy as np

background_color = "white"
qrcode_color = "black"
def change_bg():
    global background_color
    color = colorchooser.askcolor(title = "select color")
    if color[1]:
        background_color = color[1]
    

def change_qr_color():
    global qrcode_color
    color = colorchooser.askcolor(title = "select color")
    if color[1]:
        qrcode_color = color[1]

count = 0
def generate_qrcode():
    global count
    count += 1

    url_text = m_entry.url_entry.get()
    email = m_entry.text_email1.get()
    user_folder = (f"media/{email}")
    
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = constants.ERROR_CORRECT_H,
                       box_size = 5,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = qrcode_color, back_color = background_color)
    image = image.resize((404, 404))

    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    image.save(image_path)

    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)


def add_photo_area():
    file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.png;*.jpg"),))
    image = Image.open(file_path)
    image = image.resize((188,188))
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_CAB, image = imageTk, text = "")
    label_image.place(x = 6,y = 6)

def circle_qrcode():
    global count
    count += 1
    url_text = m_entry.url_entry.get()

    email = m_entry.text_email1.get()
    user_folder = (f"media/{email}")
    os.makedirs(user_folder, exist_ok = True)
    
    qr = qrcode.QRCode(version = 1,
                       error_correction = constants.ERROR_CORRECT_H,
                       box_size = 5,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)

    qr_matrix = qr.get_matrix()
    circle_size = 10
    circle_color = qrcode_color
    image_size = len(qr_matrix) * circle_size
    image = Image.new("RGB", (image_size, image_size), background_color)
    draw = ImageDraw.Draw(image)
    for row in range(len(qr_matrix)):
        for col in range(len(qr_matrix[row])):
            if qr_matrix[row][col]:
                x = circle_size * col
                y = row * circle_size
                draw.ellipse((x, y, x + circle_size, y + circle_size), fill = circle_color)
    image = image.resize((392, 392))
    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)


listbox_images = Listbox(m_app.app.frame_list_qrcode, width = 30, height = 19,bg = "#1E1E1E", fg = "white", font = m_font.font_reg)  
listbox_images.place(x = 10,y = 10)


processed_files = []
def update_image_list():
    global processed_files
    email = m_entry.text_email1.get()
    folder_path = f"media/{email}"
    current_files = os.listdir(folder_path)
    new_files = [file for file in current_files if file not in processed_files]
    for file in new_files:
        file_path = os.path.join(folder_path, file)
        listbox_images.insert(ctk.END, file_path)
        processed_files.append(file)


def personal_area():
    m_app.app.show_frame4()
    update_image_list()

def display_image(event):
    selected_index = listbox_images.curselection()
    if selected_index:
        image_path = listbox_images.get(selected_index)
        image = Image.open(image_path)
        image = image.resize((402, 402))
        tk_image = ImageTk.PhotoImage(image)
        label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE2, image = tk_image, text = "")
        label_image.place(x = 5,y = 5)

listbox_images.bind("<<ListboxSelect>>", display_image)


def add_logo():
    global count
    count += 1
    logo_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.png;*.jpg"),))
    
    url_text = m_entry.url_entry.get()

    email = m_entry.text_email1.get()
    user_folder = (f"media/{email}")
    os.makedirs(user_folder, exist_ok = True)

    qr = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(url_text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color = qrcode_color, back_color = background_color).convert("RGB")

    logo_image = Image.open(logo_path)

    logo_size = (100, 100)
    logo_image = logo_image.resize(logo_size)

    qr_width, qr_height = qr_image.size
    logo_width, logo_height = logo_image.size
    logo_position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

    qr_image.paste(logo_image, logo_position)
    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    qr_image.save(image_path)
    qr_image = qr_image.resize((404,404))

    imageTk = ImageTk.PhotoImage(qr_image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)

label_qrcodes = ctk.CTkLabel(master = m_app.app.FRAME_4,text = "Your qr-codes", font = m_font.font_auto, text_color = "black")
label_qrcodes.place(x = 250, y = 20)


def validate_password_input(text):
    pattern = f'^[a-zA-Z0-9]+$'
    if re.match(pattern, text) or text == '':
        return True
    else:
        return False
    

validate_func = m_app.app.register(validate_password_input)
m_entry.password_entry.configure(validate="key", validatecommand=(validate_func, '%P'))
m_entry.password1_entry.configure(validate="key", validatecommand=(validate_func, '%P'))
m_entry.password2_entry.configure(validate="key", validatecommand=(validate_func, '%P'))

