import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from constants import *
import random


root = tk.Tk()
root.geometry("350x470")
root.title("Movies and Shows")
root.resizable(False, False)



dict_menu = {"Animation": dict_anim, 
            "Movies": dict_movies,
            "TV Shows": dict_tv,
            "Actors and Directors": dict_act_dir
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
            widgets.pack_forget()
        
        
        if "self.frame" in globals():
            self.frame.pack_forget()

        
        self.frame = Frame(root)
        self.frame.pack(fill=BOTH, expand=1)
    
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=2)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        label_cat = Label(self.frame, text=self.name)
        label_cat.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
    
        btn_confirm = Button(self.frame, text="Confirm", command=self.confirm)
        btn_confirm.grid(row=4, column=1, padx=30, pady=1, sticky="ne")


    def create_rb_text(self):
        
        if self.rb1 is not None:
            self.rb1.destroy()
            self.rb2.destroy()
            self.rb3.destroy()
        
        self.key_list = list(self.dict.keys())
        self.value_list = list(self.dict.values())
        self.rb_text = []
        print("-------------------------------------------")
        print(self.rb_text)
        for value in self.value_list:
            if value == self.img:
                self.rb_text.append(self.key_list[self.value_list.index(value)])
                
                print(self.rb_text)
        i = 0
        while i < 2:
            while True:
                random_key = random.choice(self.key_list)
                if random_key not in self.rb_text:
                    self.rb_text.append(random_key)
                    break
            i += 1
        
        random.shuffle(self.rb_text)
        print(self.rb_text)
        
        self.selected_movie = StringVar()
        self.selected_movie.set(0)
        
        self.rb1 = Radiobutton(self.frame, text=(self.rb_text[0]), value=(self.rb_text[0]), variable=self.selected_movie)
        self.rb1.grid(row=2, column=0, padx=60, pady=1, columnspan=2, sticky="w")
        self.rb2 = Radiobutton(self.frame, text=(self.rb_text[1]), value=(self.rb_text[1]), variable=self.selected_movie)
        self.rb2.grid(row=3, column=0, padx=60, pady=1, columnspan=2, sticky="w")
        self.rb3 = Radiobutton(self.frame, text=(self.rb_text[2]), value=(self.rb_text[2]), variable=self.selected_movie)
        self.rb3.grid(row=4, column=0, padx=60, pady=1, columnspan=2, sticky="w")


    
    def show_image(self):
    
        self.img = random.choice(list(self.dict.values()))
        while self.img in self.img_list:
            self.img = random.choice(list(self.dict.values()))
        self.img_list.append(self.img)
        width, height = self.img.size
        while width > 700 or height > 400:
            width /= 1.01
            height /= 1.01
        img_resized = self.img.resize((int(width/2), int(height/2)))
        photo = ImageTk.PhotoImage(img_resized)
        label_img = Label(self.frame, image=photo)
        label_img.image = photo
        label_img.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")
        self.create_rb_text()

    def green_red(self):
        frame_right_wrong = Frame(self.frame)
        frame_right_wrong.grid(row=2, column=1, padx=30, pady=1, sticky="e", rowspan=2)
        right_wrong_bg = "white"
        self.list_right_wrong_frames = []

        for frame in range(len(self.dict)):
            row = 0 if frame < 5 else 1
            column = frame if frame < 5 else frame - 5
            frame = Frame(frame_right_wrong, bg=right_wrong_bg, borderwidth=1, relief="solid")
            frame.grid(row=row, column=column, padx=1, pady=1, sticky="nsew")
            frame.config(width=10, height=10)
            self.list_right_wrong_frames.append(frame)
    
    
    def confirm(self):
        if self.selected_movie.get() == "0":
            return

        if self.selected_movie.get() == self.key_list[self.value_list.index(self.img)]:
            result = 1
            control = 0
            while control in self.list_control:
                control += 1
            self.list_right_wrong_frames[control].config(bg="green")
            self.list_control.append(control)
            self.list_result.append(result)
        else:
            result = 0
            control = 0
            while control in self.list_control:
                control += 1
            self.list_right_wrong_frames[control].config(bg="red")
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
        frame_lose_win = Frame(self.frame, bg="white")
        frame_lose_win.pack(fill=BOTH, expand=1)
        label_result = Label(frame_lose_win, text=text)
        label_result.pack(pady=5, anchor="center")
        label_percent = Label(frame_lose_win, text=f"{self.percentage}%", bg="green" if self.percentage >= 50 else "red")
        label_percent.pack(pady=5, anchor="center") 

def choose_category(key, value):
    for widgets in root.winfo_children():
        widgets.pack_forget()

    print (key)
    category = Category(key, value)
    category.frames()
    category.show_image()
    category.green_red()

def menu():
    
    menu = Menu(root)
    root.config(menu=menu)   

    cat_menu = Menu(menu)
    menu.add_cascade(label="Categories", menu=cat_menu)
    for key, value in dict_menu.items():
        cat_menu.add_command(label=key, command=lambda key=key, value=value: choose_category(key, value))
        cat_menu.add_separator()
    cat_menu.add_command(label="Exit", command=root.quit)           
     
menu()
root.mainloop()
