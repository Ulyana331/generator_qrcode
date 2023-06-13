import qrcode 
import os
from tkinter import colorchooser
from PIL import Image, ImageTk
import modules.create_entry as m_entry
import customtkinter as ctk
import modules.create_app as m_app

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
    image = qr.make_image(fill_color = qrcode_color, back_color = background_color)
    image = image.resize((400, 400))
    image_path = os.path.join(user_folder, f"qrcode{count}.png")
    image.save(image_path)
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    label_image.place(x = 5,y = 5)





def add_logo():
    # file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.png;*.jpg"),))
    # url_text = m_entry.url_entry.get()
    # qr = qrcode.QRCode(version = 1,
    #                    error_correction = qrcode.constants.ERROR_CORRECT_H,
    #                    box_size = 6,
    #                    border = 4)
    # qr.add_data(url_text)
    # qr.make(fit = True)

    # image = qr.make_image(fill_color = "black", back_color = "white")

    # logo_image = Image.open(file_path).convert("RGBA")

    # # Масштабирование логотипа
    # logo_size = image.size[0] // 4
    # logo_image = logo_image.resize((logo_size, logo_size), Image.ANTIALIAS)

    # # Создание нового изображения с альфа-каналом
    # qr_code_with_logo = Image.new("RGBA", image.size)

    # # Копирование QR-кода на изображение с альфа-каналом
    # qr_code_with_logo.paste(image, (0, 0))

    # # Размещение логотипа посередине QR-кода
    # position = (
    #     (qr_code_with_logo.size[0] - logo_image.size[0]) // 2,
    #     (qr_code_with_logo.size[1] - logo_image.size[1]) // 2,
    # )
    # qr_code_with_logo.alpha_composite(logo_image, position)

    # # Сохранение QR-кода с логотипом
    # qr_code_with_logo.save("qr_code_with_logo.png")

    # imageTk = ImageTk.PhotoImage(qr_code_with_logo)
    # label_image = ctk.CTkLabel(m_app.app.FRAME_QR_CODE, image = imageTk, text = "")
    # label_image.place(x = 5,y = 5)
    pass


def add_photo():
    file_path = ctk.filedialog.askopenfilename(initialdir = "images/", filetypes = (("JPEG files", "*.png;*.jpg"),))
    image = Image.open(file_path)
    image = image.resize((188,188))
    imageTk = ImageTk.PhotoImage(image)
    label_image = ctk.CTkLabel(m_app.app.FRAME_CAB, image = imageTk, text = "")
    label_image.place(x = 6,y = 6)