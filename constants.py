from tkinter import *
from PIL import Image, ImageTk

FONT_LAB_CAT = ("Arial", 22)
FONT_BUTT = ("Arial", 15)
HOVER_COLOR = "#B5B5B5"
BACKGROUND_COLOR = "black"
BUTT_COLOR = "black"

# Animation
img0 = Image.open("pictures/Brave.jpg")
img1 = Image.open("pictures/Charm.jpg")
img2 = Image.open("pictures/Coco.jpg")
img3 = Image.open("pictures/Inside Out.jpg")
img4 = Image.open("pictures/Luca.jpg")
img5 = Image.open("pictures/Soul.jpg")
img6 = Image.open("pictures/The Brave Little Toaster.jpg")
img7 = Image.open("pictures/Treasure Planet.jpg")
img8 = Image.open("pictures/United.jpg")
img9 = Image.open("pictures/Zootopia.jpg")
    
dict_anim = {"Brave": img0,
            "Charm": img1, 
            "Coco": img2, 
            "Inside Out": img3, 
            "Luca": img4, 
            "Soul": img5, 
            "The Brave Little Toaster": img6, 
            "Treasure Planet": img7, 
            "United": img8, 
            "Zootopia": img9
            }

# Shows
img10 = Image.open("pictures/Breaking Bad.jpg")
img11 = Image.open("pictures/Chernobyl.jpg")
img12 = Image.open("pictures/Doctor Who.jpg")
img13 = Image.open("pictures/Friends.jpg")
img14 = Image.open("pictures/Game of Thrones.jpg")
img15 = Image.open("pictures/Seinfeld.jpg")
img16 = Image.open("pictures/Sex and the City.jpg")
img17 = Image.open("pictures/The Simpsons.jpg")
img18 = Image.open("pictures/The Sopranos.jpg")
img19 = Image.open("pictures/True Detective.jpg")

dict_tv = {"Breaking Bad": img10,
            "Chernobyl": img11, 
            "Doctor Who": img12, 
            "Friends": img13, 
            "Game of Thrones": img14, 
            "Seinfeld": img15, 
            "Sex and the City": img16, 
            "The Simpsons": img17, 
            "The Sopranos": img18, 
            "True Detective": img19
            }

# Actors and Directors
img20 = Image.open("pictures/Adrien Brody.webp")
img21 = Image.open("pictures/Alfred Hitchcock.webp")
img22 = Image.open("pictures/Christian Bale.webp")
img23 = Image.open("pictures/Joaquin Phoenix.webp")
img24 = Image.open("pictures/Johnny Depp.webp")
img25 = Image.open("pictures/Kate Winslet.webp")
img26 = Image.open("pictures/Nikolaj Coster-Waldau.webp")
img27 = Image.open("pictures/Quentin Tarantino.webp")
img28 = Image.open("pictures/Shia LaBeouf.webp")
img29 = Image.open("pictures/Steven Spielberg.webp")

dict_act_dir = {"Adrien Brody": img20,
            "Alfred Hitchcock": img21, 
            "Christian Bale": img22, 
            "Joaquin Phoenix": img23, 
            "Johnny Depp": img24, 
            "Kate Winslet": img25, 
            "Nikolaj Coster-Waldau": img26, 
            "Quentin Tarantino": img27, 
            "Shia LaBeouf": img28, 
            "Steven Spielberg": img29
            }

# Movies
img30 = Image.open("pictures/Blade Runner.jpg")
img31 = Image.open("pictures/Figth Club.jpg")
img32 = Image.open("pictures/Forrest Gump.jpg")
img33 = Image.open("pictures/Goodfellas.jpg")
img34 = Image.open("pictures/Life is Beautiful.jpg")
img35 = Image.open("pictures/Pulp Fiction.jpg")
img36 = Image.open("pictures/Scarface.jpg")
img37 = Image.open("pictures/Schindler's List.jpg")
img38 = Image.open("pictures/Seven.jpg")
img39 = Image.open("pictures/The Green Mile.jpg")

dict_movies = {"Blade Runner": img30,
            "Figth Club": img31, 
            "Forrest Gump": img32, 
            "Goodfellas": img33, 
            "Life is Beautiful": img34, 
            "Pulp Fiction": img35, 
            "Scarface": img36, 
            "Schindler's List": img37, 
            "Seven": img38, 
            "The Green Mile": img39
            }    