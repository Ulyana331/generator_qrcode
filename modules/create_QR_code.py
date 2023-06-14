import qrcode 
import os
from tkinter import colorchooser, Listbox
from PIL import Image, ImageTk, ImageDraw
import modules.create_entry as m_entry
import customtkinter as ctk
import modules.create_app as m_app
from qrcode.image.styledpil import StyledPilImage

current_index = 0
list_qrcodes = []

background_color = "white"
qrcode_color = "black"
def change_back():
    global background_color
    color = colorchooser.askcolor(title = "select color")
    if color[1]:
        background_color = color[1]
    

def change_color():
    global qrcode_color
    color = colorchooser.askcolor(title = "select color")
    if color[1]:
        qrcode_color = color[1]

count = 1
def generate_qrcode():
    global count, current_index
    count += 1

    url_text = m_entry.url_entry.get()
    email = m_entry.text_email1.get()
    user_folder = (f"media/{email}")
    
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = qrcode_color, back_color = background_color)
    image = image.resize((400, 400))
    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)

    if current_index < len(list_qrcodes):
        value = list_qrcodes[current_index]
        listbox_images.insert("end", value)
        current_index += 1

listbox_images = Listbox(m_app.app.frame_list_qrcode, width = 37, height = 10 ,bg = "#1E1E1E", fg = "white")  
listbox_images.place(x = 30,y = 1080)



def add_photo():
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
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
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

def add_logo():
    global count
    count += 1
    url_text = m_entry.url_entry.get()

    email = m_entry.text_email1.get()
    user_folder = (f"media/{email}")
    os.makedirs(user_folder, exist_ok = True)
    
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(image_factory = StyledPilImage, embeded_image_path = "logo.png")
    image = image.resize((392, 392))
    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)
