import qrcode 
import os
from PIL import Image, ImageTk
import modules.create_entry as m_entry
import customtkinter as ctk
import modules.create_app as m_app

def generate_qrcode():
    url_text = m_entry.url_entry.get()
    user_folder = "media/user1"
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = "black", back_color = "white")
    image_path = os.path.join(user_folder, "qrcode.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)


def change_back():
    url_text = m_entry.url_entry.get()
    user_folder = "media/user1"
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = "black", back_color = "red")
    image_path = os.path.join(user_folder, "qrcode.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)

def change_color():
    url_text = m_entry.url_entry.get()
    user_folder = "media/user1"
    os.makedirs(user_folder, exist_ok = True)
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 6,
                       border = 4)
    qr.add_data(url_text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = "blue", back_color = "white")
    image_path = os.path.join(user_folder, "qrcode.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)
