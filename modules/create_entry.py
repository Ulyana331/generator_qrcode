import customtkinter as ctk
import modules.create_app as m_app

text_url = ctk.StringVar()
text_url.set("Enter URL")
def handle_focus_in(event):
    if url_entry.get() == text_url.get():
        url_entry.delete(0,"end")
        url_entry.config(fg = "#000000")
def handle_focus_out(event):
    if url_entry.get() == "":
        url_entry.insert(0,text_url.get())
        url_entry.config(fg = "#A9A9A9")
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
url_entry.configure()
url_entry.bind("<FocusIn>", handle_focus_in)
url_entry.bind("<FocusOut>", handle_focus_out)

url_entry.place(x = 26,y = 78)


text_name = ctk.StringVar()
text_name.set("Enter Name")
def handle_focus_in(event):
    if name_entry.get() == text_name.get():
        name_entry.delete(0,"end")
        name_entry.config(fg = "#000000")
def handle_focus_out(event):
    if name_entry.get() == "":
        name_entry.insert(0,text_name.get())
        name_entry.config(fg = "#A9A9A9")
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
name_entry.configure()
name_entry.bind("<FocusIn>", handle_focus_in)
name_entry.bind("<FocusOut>", handle_focus_out)

name_entry.place(x = 161,y = 70)


text_email = ctk.StringVar()
text_email.set("Enter Email")
def handle_focus_in(event):
    if email_entry.get() == text_email.get():
        email_entry.delete(0,"end")
        email_entry.config(fg = "#000000")
def handle_focus_out(event):
    if email_entry.get() == "":
        email_entry.insert(0,text_email.get())
        email_entry.config(fg = "#A9A9A9")
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
email_entry.configure()
email_entry.bind("<FocusIn>", handle_focus_in)
email_entry.bind("<FocusOut>", handle_focus_out)

email_entry.place(x = 161,y = 152)


text_password = ctk.StringVar()
text_password.set("Enter Password")
def handle_focus_in(event):
    if password_entry.get() == text_password.get():
        password_entry.delete(0,"end")
        password_entry.config(fg = "#000000")
def handle_focus_out(event):
    if password_entry.get() == "":
        password_entry.insert(0,text_password.get())
        password_entry.config(fg = "#A9A9A9")
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
password_entry.configure()
password_entry.bind("<FocusIn>", handle_focus_in)
password_entry.bind("<FocusOut>", handle_focus_out)

password_entry.place(x = 161,y = 242)


text_password2 = ctk.StringVar()
text_password2.set("Confirm Password")
def handle_focus_in(event):
    if password2_entry.get() == text_password2.get():
        password2_entry.delete(0,"end")
        password2_entry.config(fg = "#000000")
def handle_focus_out(event):
    if password2_entry.get() == "":
        password2_entry.insert(0,text_password2.get())
        password2_entry.config(fg = "#A9A9A9")
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
password2_entry.configure()
password2_entry.bind("<FocusIn>", handle_focus_in)
password2_entry.bind("<FocusOut>", handle_focus_out)

password2_entry.place(x = 161,y = 332)



text_email1 = ctk.StringVar()
text_email1.set("Enter Email")
def handle_focus_in(event):
    if email1_entry.get() == text_email1.get():
        email1_entry.delete(0,"end")
        email1_entry.config(fg = "#000000")
def handle_focus_out(event):
    if email1_entry.get() == "":
        email1_entry.insert(0,text_email1.get())
        email1_entry.config(fg = "#A9A9A9")
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
email1_entry.configure()
email1_entry.bind("<FocusIn>", handle_focus_in)
email1_entry.bind("<FocusOut>", handle_focus_out)

email1_entry.place(x = 161,y = 186)


text_password1 = ctk.StringVar()
text_password1.set("Enter Password")
def handle_focus_in(event):
    if password1_entry.get() == text_password1.get():
        password1_entry.delete(0,"end")
        password1_entry.config(fg = "#000000")
def handle_focus_out(event):
    if password1_entry.get() == "":
        password1_entry.insert(0,text_password1.get())
        password1_entry.config(fg = "#A9A9A9")
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
password1_entry.configure()
password1_entry.bind("<FocusIn>", handle_focus_in)
password1_entry.bind("<FocusOut>", handle_focus_out)

password1_entry.place(x = 161,y = 268)


