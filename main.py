import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkImage
from constants import *
import random
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

root = customtkinter.CTk()
root.geometry("350x470")
root.title("Movies and Shows")
root.resizable(False, False)
root.configure(fg_color=BACKGROUND_COLOR)

root_bg = Image.open("pictures/Background.jpg")
width, height = root_bg.size
while width > 350:
    width /= 1.01
while height > 470:    
    height /= 1.01
root_bg = CTkImage(root_bg, size=(width, height))
root_bg_label = customtkinter.CTkLabel(root, 
                                       image=root_bg, 
                                       text=" "
                                       )
root_bg_label.grid(row=1, 
                   column=0, 
                   sticky="nsew", 
                   pady=2
                   )

root.grid_rowconfigure(0, weight=1)  
root.grid_rowconfigure(1, weight=25)
root.grid_columnconfigure(0, weight=1)

dict_menu = {"Animation": dict_anim, 
            "Movies": dict_movies,
            "TV Shows": dict_tv,
            "Actors and Directors": dict_act_dir,
            "Exit": root.quit()
            }

class Category():
    def __init__(self, name, dict):
        self.name = name
        self.dict = dict
        self.rb1 = None
        self.rb2 = None
        self.rb3 = None
        self.img_list = [] 
        self.list_result = []
        self.list_control = []
    
    def frames(self):
        for widgets in root.winfo_children():
            if widgets != cat_menu:
                widgets.destroy()
        
        
        if "self.frame" in globals():
            self.frame.destroy()

        self.frame = customtkinter.CTkFrame(root, 
                                            fg_color=BACKGROUND_COLOR
                                            )
        self.frame.grid(row=1, 
                        column=0, 
                        sticky="nsew", 
                        pady=2
                        )

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=20)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        
        label_cat = customtkinter.CTkLabel(self.frame, 
                                           text=self.name, 
                                           font=FONT_LAB_CAT, 
                                           bg_color=BACKGROUND_COLOR
                                           )
        label_cat.grid(row=0, 
                       column=0, 
                       padx=5, 
                       pady=5, 
                       sticky="nsew", 
                       columnspan=2
                       )
    
        btn_confirm = customtkinter.CTkButton(self.frame, 
                                              text="Confirm", 
                                              fg_color=BUTT_COLOR, 
                                              font=FONT_BUTT, 
                                              width=10, 
                                              height=10, 
                                              corner_radius=10, 
                                              hover= True, 
                                              hover_color=HOVER_COLOR, 
                                              command=self.confirm
                                              )
        btn_confirm.grid(row=4, 
                         column=1, 
                         padx=20, 
                         pady=1, 
                         sticky="ne"
                         )

    def create_rb_text(self):
        
        if self.rb1 is not None:
            self.rb1.destroy()
            self.rb2.destroy()
            self.rb3.destroy()
        
        self.key_list = list(self.dict.keys())
        self.value_list = list(self.dict.values())
        self.rb_text = []
    
        for value in self.value_list:
            if value == self.img:
                self.rb_text.append(self.key_list[self.value_list.index(value)])
                 
        i = 0
        while i < 2:
            while True:
                random_key = random.choice(self.key_list)
                if random_key not in self.rb_text:
                    self.rb_text.append(random_key)
                    break
            i += 1
        
        random.shuffle(self.rb_text)
       
        
        self.selected_movie = StringVar()
        self.selected_movie.set(0)
        
        self.rb1 = customtkinter.CTkRadioButton(self.frame, 
                                                fg_color=HOVER_COLOR, 
                                                hover=True, 
                                                hover_color=HOVER_COLOR, 
                                                radiobutton_height=12, 
                                                radiobutton_width=12, 
                                                text=(self.rb_text[0]), 
                                                value=(self.rb_text[0]), 
                                                variable=self.selected_movie
                                                )
        self.rb1.grid(row=2, 
                      column=0, 
                      padx=60, 
                      pady=1, 
                      columnspan=2, 
                      sticky="sw"
                      )
        self.rb2 = customtkinter.CTkRadioButton(self.frame, 
                                                fg_color=HOVER_COLOR, 
                                                hover=True, 
                                                hover_color=HOVER_COLOR, 
                                                radiobutton_height=12, 
                                                radiobutton_width=12, 
                                                text=(self.rb_text[1]), 
                                                value=(self.rb_text[1]), 
                                                variable=self.selected_movie
                                                )
        self.rb2.grid(row=3, 
                      column=0, 
                      padx=60, 
                      pady=1, 
                      columnspan=2, 
                      sticky="w"
                      )
        self.rb3 = customtkinter.CTkRadioButton(self.frame, 
                                                fg_color=HOVER_COLOR, 
                                                hover=True, 
                                                hover_color=HOVER_COLOR, 
                                                radiobutton_height=12, 
                                                radiobutton_width=12, 
                                                text=(self.rb_text[2]), 
                                                value=(self.rb_text[2]), 
                                                variable=self.selected_movie
                                                )
        self.rb3.grid(row=4, 
                      column=0, 
                      padx=60, 
                      pady=1, 
                      columnspan=2, 
                      sticky="nw"
                      )
    
    def show_image(self):
    
        self.img = random.choice(list(self.dict.values()))
        while self.img in self.img_list:
            self.img = random.choice(list(self.dict.values()))
        self.img_list.append(self.img)
        width, height = self.img.size
        while width > 700:
            width /= 1.01
        while height > 400:    
            height /= 1.01
        photo = CTkImage(self.img, size=(width/2, height/2))
        label_img = customtkinter.CTkLabel(self.frame, 
                                           image=photo, 
                                           text=" ", 
                                           bg_color=BACKGROUND_COLOR
                                           )
        label_img.image = photo
        label_img.grid(row=1, 
                       column=0, 
                       columnspan=2, 
                       pady=5, 
                       sticky="nsew"
                       )
        self.create_rb_text()

    def green_red(self):
        frame_right_wrong = customtkinter.CTkFrame(self.frame, 
                                                   fg_color=BACKGROUND_COLOR
                                                   )
        frame_right_wrong.grid(row=2, 
                               column=1, 
                               padx=20, 
                               pady=1, 
                               sticky="e", 
                               rowspan=2
                               )
        self.list_right_wrong_frames = []

        for frame in range(len(self.dict)):
            row = 0 if frame < 5 else 1
            column = frame if frame < 5 else frame - 5
            frame = customtkinter.CTkFrame(frame_right_wrong, 
                                           fg_color=HOVER_COLOR
                                           )
            frame.grid(row=row, 
                       column=column, 
                       padx=1, 
                       pady=1, 
                       sticky="nsew"
                       )
            frame.configure(width=10, 
                            height=10, 
                            corner_radius=5, 
                            border_color=HOVER_COLOR
                            )
            self.list_right_wrong_frames.append(frame)
    
    def confirm(self):
        if self.selected_movie.get() == "0":
            return

        if self.selected_movie.get() == self.key_list[self.value_list.index(self.img)]:
            result = 1
            control = 0
            while control in self.list_control:
                control += 1
            self.list_right_wrong_frames[control].configure(fg_color="green")
            self.list_control.append(control)
            self.list_result.append(result)
        else:
            result = 0
            control = 0
            while control in self.list_control:
                control += 1
            self.list_right_wrong_frames[control].configure(fg_color="red")
            self.list_control.append(control)
            self.list_result.append(result)
            
        if len(self.list_control) < len(self.dict):
            self.show_image()
        else:
            self.percentage = int(sum(self.list_result)*100/(len(self.list_result)))
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            
            if self.percentage >= 50:  
                self.lose_win("CONGRATULATIONS")
            else:
                self.lose_win("NEXT TIME")

    def lose_win(self, text):
        label_result = customtkinter.CTkLabel(self.frame, 
                                              text=text, 
                                              font=FONT_LAB_CAT
                                              )
        label_result.grid(row=0,
                          pady=50,
                          columnspan=2 
                          )
        label_percent = customtkinter.CTkLabel(self.frame, 
                                               width=50,
                                               height=10,
                                               font=FONT_LAB_CAT, 
                                               text=f"{self.percentage}%", 
                                               bg_color="green" if self.percentage >= 50 else "red"
                                               )
        label_percent.grid(row=1, 
                           columnspan=2
                           ) 
    
def choose_category(key, value):
    category = Category(key, value)
    category.frames()
    category.show_image()
    category.green_red()
    
def menu():
    global cat_menu
    optionmenu_var = customtkinter.StringVar(value="Categories")
    cat_menu = customtkinter.CTkOptionMenu(root,
                                           dynamic_resizing=True,
                                           width=10,
                                           height=20,
                                           dropdown_fg_color=BUTT_COLOR,
                                           dropdown_hover_color=HOVER_COLOR,
                                           button_color=BUTT_COLOR,
                                           button_hover_color=HOVER_COLOR,
                                           dropdown_font=FONT_BUTT,
                                           font=FONT_BUTT,
                                           fg_color=BUTT_COLOR,
                                           corner_radius=5,
                                           hover=True,
                                           values=list(dict_menu.keys()), 
                                           variable=optionmenu_var,
                                           command=optionmenu_callback
                                           )
    cat_menu.grid(row=0, 
                  column=0, 
                  sticky="w", 
                  pady=2
                  ) 
    
def optionmenu_callback(selection):
    if selection == "Exit":
        root.quit()
    else:
        choose_category(selection, dict_menu[selection])
        
menu()

root.mainloop()
