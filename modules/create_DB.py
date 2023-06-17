import os
import sqlite3
import modules.create_entry as m_entry
import modules.create_app as m_app
import customtkinter as ctk
import modules.create_font as m_font

connection_Auto = sqlite3.connect("database_autorization.db")
cursor_Auto = connection_Auto.cursor()
cursor_Auto.execute("CREATE TABLE IF NOT EXISTS Users(email TEXT, password TEXT)")


def save_data_autorization():
    email = m_entry.text_email1.get()
    password = m_entry.text_password1.get()
    cursor_Auto.execute("INSERT INTO Users(email, password) VALUES (?,?)",(email, password))
    connection_Auto.commit()

    quarry = "SELECT * FROM Users WHERE email = ? AND password = ?"
    cursor_reg.execute(quarry,(email, password))
    user = cursor_reg.fetchone()

    if user is not None:
        m_app.app.show_frame1()
    else:
        label_not_auto = ctk.CTkLabel(master = m_app.app.FRAME_3, text = 'No such account', font = m_font.font_auto)
        label_not_auto.place(x = 240,y= 90)
        label_not_auto2 = ctk.CTkLabel(master = m_app.app.FRAME_3, text = 'Register!', font = m_font.font_auto)
        label_not_auto2.place(x = 280,y= 130)
    # connection_Auto.close()
    

connection_reg = sqlite3.connect("database_registration.db")
cursor_reg = connection_reg.cursor()
cursor_reg.execute("CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY, Name TEXT, email TEXT, password TEXT, password_confirm TEXT)")
def save_data_registration():
    email = m_entry.text_email.get()
    password = m_entry.text_password.get()
    name = m_entry.text_name.get()
    password_confirm = m_entry.text_password2.get()
    
    if not email or not name:
        label_not_reg = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "No email or name entered", font = m_font.font_reg)
        label_not_reg.place(x = 340,y = 215) 
    elif password != password_confirm:
        label_not_reg = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Password mismatch!       ", font = m_font.font_reg)
        label_not_reg.place(x = 340,y = 215)  
    elif password == password_confirm and name and email:
        label_not_reg = ctk.CTkLabel(master = m_app.app.FRAME_2, text = "Successful registration    ", font = m_font.font_reg)
        label_not_reg.place(x = 340,y = 215)   
        cursor_reg.execute("INSERT INTO Users(Name ,email, password, password_confirm) VALUES (?,?,?,?)",(name, email, password, password_confirm))
    connection_reg.commit()
    # connection_reg.close() 


cursor_Auto.execute("SELECT email, password, COUNT(*) FROM users GROUP BY email, password")
duplicate_rows = cursor_Auto.fetchall()

for row in duplicate_rows:
    email = row[0]
    password = row[1]
    cursor_Auto.execute("DELETE FROM users WHERE email=? AND password=?", (email, password))