import customtkinter as ctk
import modules.create_QR_code as m_qr
import modules.create_app as m_app
import modules.create_DB as m_DB
import modules.create_font as m_font

create_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 240,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    command = m_qr.generate_qrcode,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    text = "Create QR-code"
)
create_button.place(x = 431,y = 429)

bg_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    command = m_qr.change_bg,
    bg_color = "transparent",
    text = "Select background color"
)
bg_button.place(x = 26, y = 160)

image_color_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    command = m_qr.change_qr_color,
    text = "Select image color"
)
image_color_button.place(x = 26, y = 250)

add_logo_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    text = "Add logo to QR-code",
    command = m_qr.add_logo
)
add_logo_button.place(x = 26, y = 340)

design_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 370,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    text = "Select image design QR-code",
    command = m_qr.triangle
)
design_button.place(x = 26, y = 430)

confirm_button = ctk.CTkButton(
    master = m_app.app.FRAME_2,
    width = 159,
    height = 61,
    corner_radius = 15,
    border_width = 3,
    command = m_DB.save_data_registration,
    border_color = "#C1FFC1",
    fg_color = "#282828",
    bg_color = "transparent",
    text = "Confirm")

confirm_button.place(x = 262, y = 409)

login_button = ctk.CTkButton(
    master = m_app.app.FRAME_2,
    width = 253,
    height = 37,
    corner_radius = 15,
    fg_color = "#8470FF",
    bg_color = "transparent",
    text_color = "black",
    text = "Or log in",
    command = m_app.app.show_frame3)

login_button.place(x = 215, y = 470)

enter_button = ctk.CTkButton(
    master = m_app.app.FRAME_3,
    width = 159,
    height = 61,
    corner_radius = 15,
    fg_color = "#282828",
    command = m_DB.save_data_autorization,
    bg_color = "transparent",
    border_width=3,
    border_color= "#C1FFC1",
    text = "Enter")

enter_button.place(x = 266, y = 358)

registration_button = ctk.CTkButton(
    master = m_app.app.FRAME_3,
    width = 253,
    height = 37,
    corner_radius = 15,
    fg_color = "#8470FF",
    bg_color = "transparent",
    text_color = "black",
    text = "Or sing up",
    command = m_app.app.show_frame2)

registration_button.place(x = 221, y = 433)

add_photo_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 70,
    height = 45,
    corner_radius = 15,
    fg_color = "#282828",
    bg_color = "transparent",
    text_color = "white",
    text = "Add photo",
    font = m_font.font_entry,
    border_color = "#C1FFC1",
    border_width = 3,
    command = m_qr.add_photo_area
)
add_photo_button.place(x = 420, y = 100)

personal_area_button = ctk.CTkButton(
    master = m_app.app.FRAME_1,
    width = 70,
    height = 45,
    corner_radius = 15,
    fg_color = "#282828",
    bg_color = "transparent",
    text_color = "white",
    text = "Personal area",
    font = m_font.font_entry,
    border_color = "#C1FFC1",
    border_width = 3,
    command = m_qr.personal_area
)
personal_area_button.place(x = 420, y = 40)

back_button = ctk.CTkButton(
    master = m_app.app.FRAME_4,
    width = 80,
    height = 45,
    corner_radius = 15,
    fg_color = "#282828",
    bg_color = "transparent",
    text_color = "white",
    text = "Back",
    font = m_font.font_entry,
    border_color = "#C1FFC1",
    border_width = 3,
    command = m_app.app.show_frame_1
)
back_button.place(x = 20, y = 440)