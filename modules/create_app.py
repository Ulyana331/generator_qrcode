import customtkinter as ctk
import modules.create_frame as m_frame 
import os

def search_path(name_file):
    path = __file__.split("\\") 
    for i in range(2):
        del path[-1]
    path = "\\".join(path)
    path = os.path.join(path, name_file)
    print(path)
    return path

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{600}+{160}")
        self.resizable(False,False)
        self.title("Generator QR-code")
        self.iconbitmap(search_path("icon.ico"))
        self.FRAME_1 = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 696,
                                       height = 515,
                                       border_width = 5,
                                       fg_color = "#8470FF",
                                       border_color = "#1E1E1E",
                                       corner_radius = 15)
        # self.FRAME_1.place(x = 0, y = 0)
        
        self.FRAME_QR_CODE = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 240,
                                       height = 240,
                                       border_width = 5,
                                       fg_color = "#282828",
                                       border_color = "#C1FFC1",
                                       bg_color = "#8470FF",
                                       corner_radius = 15)
        self.FRAME_QR_CODE.place(x = 431, y = 160)

        self.FRAME_CAB = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 120,
                                       height = 120,
                                       border_width = 5,
                                       fg_color = "#282828",
                                       border_color = "#C1FFC1",
                                       bg_color = "#8470FF",
                                       corner_radius = 15)
        self.FRAME_CAB.place(x = 551, y = 25)

        font_label = ctk.CTkFont(family = "Times New Roman",
                         size = 24,
                         weight = "bold")
        
        self.LABEL = ctk.CTkLabel(master = self.FRAME_1,
                                  width = 250,
                                  height = 60,
                                  text = "Generator QR-code",
                                  text_color = "black",
                                  font = font_label)
        self.LABEL.place(x = 150, y = 10)

        self.FRAME_2 = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 696,
                                       height = 515,
                                       border_width = 5,
                                       fg_color = "#8470FF",
                                       border_color = "#1E1E1E",
                                       corner_radius = 15)
        # self.FRAME_2.place(x = 0, y = 0)

        self.LABEL_REGISTRATION = ctk.CTkLabel(master = self.FRAME_2,
                                  width = 250,
                                  height = 60,
                                  text = "Registration",
                                  text_color = "black",
                                  font = font_label)
        self.LABEL_REGISTRATION.place(x = 225, y = 5)


        self.FRAME_3 = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 696,
                                       height = 515,
                                       border_width = 5,
                                       fg_color = "#8470FF",
                                       border_color = "#1E1E1E",
                                       corner_radius = 15)
        # self.FRAME_3.place(x = 0, y = 0)


        self.LABEL_AUTORIZATION = ctk.CTkLabel(master = self.FRAME_3,
                                  width = 250,
                                  height = 60,
                                  text = "Autorization",
                                  text_color = "black",
                                  font = font_label)
        self.LABEL_AUTORIZATION.place(x = 200, y = 10)

        self.FRAME_4 = m_frame.MyFrame(text = "", 
                                       master = self,
                                       width = 696,
                                       height = 515,
                                       border_width = 5,
                                       fg_color = "#8470FF",
                                       border_color = "#1E1E1E",
                                       corner_radius = 15)
        
        self.FRAME_QR_CODE2 = m_frame.MyFrame(text = "", 
                                       master = self.FRAME_4,
                                       width = 240,
                                       height = 240,
                                       border_width = 5,
                                       fg_color = "#282828",
                                       border_color = "#C1FFC1",
                                       bg_color = "#8470FF",
                                       corner_radius = 15)
        self.FRAME_QR_CODE2.place(x = 431, y = 100)
        self.frame_list_qrcode = m_frame.MyFrame(text = "", 
                                       master = self.FRAME_4,
                                       width = 200,
                                       height = 280,
                                       border_width = 2,
                                       fg_color = "#282828",
                                       border_color = "#C1FFC1",
                                       bg_color = "#8470FF",
                                       corner_radius = 15)
        self.frame_list_qrcode.place(x = 20, y = 100)
        self.show_frame3()
        
    def show_frame1(self):
        self.FRAME_1.pack()
        self.FRAME_3.pack_forget()

    def show_frame2(self):
        self.FRAME_2.pack()
        self.FRAME_3.pack_forget()

    def show_frame3(self):
        self.FRAME_3.pack()
        self.FRAME_2.pack_forget()

    def show_frame4(self):
        self.FRAME_4.pack()
        self.FRAME_1.pack_forget()
        
    def show_frame_1(self):
        self.FRAME_1.pack()
        self.FRAME_4.pack_forget()
        
app = App(696, 515)