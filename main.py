from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Movies and Shows")
root.geometry("350x350")

menu = Menu(root)
root.config(menu=menu)



def animation():
    global frame_anim
    if "frame_anim" in globals():
        frame_anim.pack_forget()
    
    frame_anim = Frame(root)
    frame_anim.pack(fill=BOTH, expand=1)
    
    def create_rb_text():
        global rb1, rb2, rb3
        if "rb1" in globals():
            rb1.grid_forget()
            rb2.grid_forget()
            rb3.grid_forget()
        global rb_text
        global key_list
        global value_list
        rb_text = []
        key_list = list(img_dict.keys())
        value_list = list(img_dict.values())
        for value in value_list:
            if value == img:
                rb_text.append(key_list[value_list.index(value)])

        i = 0
        while i < 2:
            while True:
                random_key = random.choice(key_list)
                if random_key not in rb_text:
                    rb_text.append(random_key)
                    break
            i += 1
        
        random.shuffle(rb_text)

        global selected_movie
        selected_movie = StringVar()
        selected_movie.set(0)
        
        
        rb1 = Radiobutton(frame_anim, text=(rb_text[0]), value=(rb_text[0]), variable=selected_movie)
        rb1.grid(row=2, column=0, padx=60, pady=1, columnspan=2, sticky="w")
        rb2 = Radiobutton(frame_anim, text=(rb_text[1]), value=(rb_text[1]), variable=selected_movie)
        rb2.grid(row=3, column=0, padx=60, pady=1, columnspan=2, sticky="w")
        rb3 = Radiobutton(frame_anim, text=(rb_text[2]), value=(rb_text[2]), variable=selected_movie)
        rb3.grid(row=4, column=0, padx=60, pady=1, columnspan=2, sticky="w")
        
    list_control = []   
    def confirm():
        if selected_movie.get() == "0":
            return
        
        
        if selected_movie.get() == key_list[value_list.index(img)]:
            control = 0
            while control in list_control:
                control += 1
            list_right_wrong_frames[control].config(bg="green")
            list_control.append(control)
        else:
            control = 0
            while control in list_control:
                control += 1
            list_right_wrong_frames[control].config(bg="red")
            list_control.append(control)

            
                    
            
        
        show_image()
        
    def show_image():
        global img
        img = random.choice(list(img_dict.values()))
        if img in img_list:
            show_image()
        img_list.append(img)
        width, height = img.size
        while width > 700 or height > 400:
            width /= 1.01
            height /= 1.01
        img_resized = img.resize((int(width/2), int(height/2)))
        photo = ImageTk.PhotoImage(img_resized)
        label_img = Label(frame_anim, image=photo)
        label_img.image = photo
        label_img.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")
        create_rb_text()

    
    
    img0 = Image.open("pictures/animation/Brave.jpg")
    img1 = Image.open("pictures/animation/Charm.jpg")
    img2 = Image.open("pictures/animation/Coconut.jpg")
    img3 = Image.open("pictures/animation/Inside Out.jpg")
    img4 = Image.open("pictures/animation/Luca.jpg")
    img5 = Image.open("pictures/animation/Soul.jpg")
    img6 = Image.open("pictures/animation/The Brave Little Toaster.jpg")
    img7 = Image.open("pictures/animation/Treasure Planet.jpg")
    img8 = Image.open("pictures/animation/United.jpg")
    img9 = Image.open("pictures/animation/Zootopia.jpg")
    
    global img_dict
    img_dict = {"Brave": img0,
                "Charm": img1, 
                "Coconut": img2, 
                "Inside Out": img3, 
                "Luca": img4, 
                "Soul": img5, 
                "The Brave Little Toaster": img6, 
                "Treasure Planet": img7, 
                "United": img8, 
                "Zootopia": img9
                }
    
    global img_list
    img_list = []
    show_image()


    frame_anim.grid_rowconfigure(0, weight=1)
    frame_anim.grid_rowconfigure(1, weight=2)
    frame_anim.grid_rowconfigure(2, weight=1)
    frame_anim.grid_rowconfigure(3, weight=1)
    frame_anim.grid_rowconfigure(4, weight=1)
    frame_anim.grid_columnconfigure(0, weight=1)
    frame_anim.grid_columnconfigure(1, weight=1)



    label_cat = Label(frame_anim, text="Animation")
    label_cat.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)

    
    
    
    global frame_right_wrong
    frame_right_wrong = Frame(frame_anim)
    frame_right_wrong.grid(row=2, column=1, padx=30, pady=1, sticky="e", rowspan=2)
    list_right_wrong_frames = []
    right_wrong_bg = "white"
    
    for frame in range(len(img_dict)):
        row = 0 if frame < 5 else 1
        column = frame if frame < 5 else frame - 5
        frame = Frame(frame_right_wrong, bg=right_wrong_bg, borderwidth=1, relief="solid")
        frame.grid(row=row, column=column, padx=1, pady=1, sticky="nsew")
        frame.config(width=10, height=10)
        list_right_wrong_frames.append(frame)

    btn_confirm = Button(frame_anim, text="Confirm", command=confirm)
    btn_confirm.grid(row=4, column=1, padx=30, pady=1, sticky="ne")
    

cat_menu = Menu(menu)
menu.add_cascade(label="Categories", menu=cat_menu)
cat_menu.add_command(label="Animation", command=animation)
cat_menu.add_separator()
cat_menu.add_command(label="Oscar Winners")
cat_menu.add_separator()
cat_menu.add_command(label="TV Shows")
cat_menu.add_separator()
cat_menu.add_command(label="Actors and Directors")
cat_menu.add_separator()
cat_menu.add_command(label="Exit", command=root.quit)






root.mainloop()


