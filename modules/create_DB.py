import os
import sqlite3
import modules.create_entry as m_entry

connection_Auto = sqlite3.connect("database_autorization.db")
cursor_Auto = connection_Auto.cursor()
cursor_Auto.execute("CREATE TABLE IF NOT EXISTS Users(email TEXT, password TEXT)")
def save_data_autorization():
    email = m_entry.text_email1.get()
    password = m_entry.text_password1.get()
    cursor_Auto.execute("INSERT INTO Users(email, password) VALUES (?,?)",(email, password))
    connection_Auto.commit()
    print("данні збережено!")
    connection_Auto.close()

connection_reg = sqlite3.connect("database_registration.db")
cursor_reg = connection_reg.cursor()
cursor_reg.execute("CREATE TABLE IF NOT EXISTS Users(Name TEXT, email TEXT, password TEXT, password_confirm TEXT)")
def save_data_registration():
    email = m_entry.text_email.get()
    password = m_entry.text_password.get()
    name = m_entry.text_name.get()
    password_confirm = m_entry.text_password2.get()
    cursor_reg.execute("INSERT INTO Users(Name ,email, password, password_confirm) VALUES (?,?,?,?)",(name, email, password, password_confirm))
    connection_reg.commit()
    print("данні збережено!")
    connection_reg.close()