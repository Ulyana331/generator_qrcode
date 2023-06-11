import customtkinter as ctk
import modules.create_app as m_app
import modules.create_font as m_font

label_url = ctk.CTkLabel(master = m_app.app.FRAME_1, text = "Enter url", font = m_font.font_entry)
label_url.place(x = 35, y = 45)
text_url = ctk.StringVar()
url_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_1,
    width = 370,
    height = 53,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_url
)

url_entry.place(x = 26,y = 78)

label_name = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Enter name", font = m_font.font_entry)
label_name.place(x = 170, y = 40)

text_name = ctk.StringVar()
name_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_2,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_name
)

name_entry.place(x = 161,y = 70)

label_email = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Enter email", font = m_font.font_entry)
label_email.place(x = 170, y = 130)

text_email = ctk.StringVar()
email_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_2,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_email
)

email_entry.place(x = 161,y = 152)

label_password = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Enter password", font = m_font.font_entry)
label_password.place(x = 170, y = 215)
text_password = ctk.StringVar()
password_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_2,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_password
)
password_entry.place(x = 161,y = 242)

label_password2 = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Enter confirm password", font = m_font.font_entry)
label_password2.place(x = 170, y = 305)
text_password2 = ctk.StringVar()
password2_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_2,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_password2
)
password2_entry.place(x = 161,y = 332)


label_email1 = ctk.CTkLabel(master = m_app.app.FRAME_3, text = "Enter email", font = m_font.font_entry)
label_email1.place(x = 170, y = 140)
text_email1 = ctk.StringVar()
email1_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_3,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_email1
)

email1_entry.place(x = 161,y = 176)

label_password1 = ctk.CTkLabel(master = m_app.app.FRAME_3, text = "Enter password", font = m_font.font_entry)
label_password1.place(x = 170, y = 240)
text_password1 = ctk.StringVar()
password1_entry = ctk.CTkEntry(
    master = m_app.app.FRAME_3,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    textvariable = text_password1
)

password1_entry.place(x = 161,y = 268)


