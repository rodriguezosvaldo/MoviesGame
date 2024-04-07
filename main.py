from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Movies and Shows")
root.geometry("500x500")

menu = Menu(root)
root.config(menu=menu)



def animation():
    frame_anim = Frame(root)
    frame_anim.pack(fill=BOTH, expand=1)
    
    def counter():
        pass

    def confirm():
        pass

    def create_lb_columns():
        for index, element in enumerate(list_right_wrong_labels):
            if 0 <= index <= 4:
                return index
            elif 5 <= index <= 9:
                return index
                

    def create_lb_rows():
        for index, element in enumerate(list_right_wrong_labels):
            if 0 <= index <= 4:
                return 0
            else:
                return 1

    frame_anim.grid_rowconfigure(0, weight=1)
    frame_anim.grid_rowconfigure(1, weight=1)
    frame_anim.grid_rowconfigure(2, weight=1)
    frame_anim.grid_rowconfigure(3, weight=1)
    frame_anim.grid_rowconfigure(4, weight=1)


    label_cat = Label(frame_anim, text="Animation")
    label_cat.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    label_counter = Label(frame_anim, text=counter)
    label_counter.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    img = Image.open("pictures/animation/Charm.jpg")
    width, height = img.size
    img = img.resize((int(width/2), int(height/2)))
    photo = ImageTk.PhotoImage(img)
    label_img = Label(frame_anim, image=photo)
    label_img.image = photo
    label_img.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

    global selected_movie
    selected_movie = IntVar()
    selected_movie.set(0)

    rb1 = Radiobutton(frame_anim, text="Charm", value=1, variable=selected_movie)
    rb1.grid(row=2, column=0, pady=5, sticky="nsew")
    rb2 = Radiobutton(frame_anim, text="The Boss Baby", value=2, variable=selected_movie)
    rb2.grid(row=3, column=0, pady=5, sticky="nsew")
    rb3 = Radiobutton(frame_anim, text="The Emoji Movie", value=3, variable=selected_movie)
    rb3.grid(row=4, column=0, pady=5, sticky="nsew")

    frame_right_wrong = Frame(frame_anim)
    frame_right_wrong.grid(row=2, column=1, pady=5, sticky="nsew")
    list_right_wrong_labels = []
    right_wrong_bg = "green"
    
    for label in range(10):
        row = 0 if label < 5 else 1
        column = label if label < 5 else label - 5
        label = Label(frame_right_wrong, text="", bg=right_wrong_bg, relief="solid")
        label.grid(row=row, column=column, sticky="nsew")
        list_right_wrong_labels.append(label)

    btn_confirm = Button(frame_anim, text="Confirm", command=confirm)
    btn_confirm.grid(row=4, column=1, pady=5, sticky="nsew")



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


