from tkinter import *
from PIL import Image, ImageTk

FONT_LAB_CAT = ("Arial", 22)
FONT_BUTT = ("Arial", 15)
HOVER_COLOR = "#B5B5B5"
BACKGROUND_COLOR = "black"
BUTT_COLOR = "black"

# Animation
img0 = Image.open("pictures/animation/Brave.jpg")
img1 = Image.open("pictures/animation/Charm.jpg")
img2 = Image.open("pictures/animation/Coco.jpg")
img3 = Image.open("pictures/animation/Inside Out.jpg")
img4 = Image.open("pictures/animation/Luca.jpg")
img5 = Image.open("pictures/animation/Soul.jpg")
img6 = Image.open("pictures/animation/The Brave Little Toaster.jpg")
img7 = Image.open("pictures/animation/Treasure Planet.jpg")
img8 = Image.open("pictures/animation/United.jpg")
img9 = Image.open("pictures/animation/Zootopia.jpg")
    
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
img10 = Image.open("pictures/tv shows/Breaking Bad.jpg")
img11 = Image.open("pictures/tv shows/Chernobyl.jpg")
img12 = Image.open("pictures/tv shows/Doctor Who.jpg")
img13 = Image.open("pictures/tv shows/Friends.jpg")
img14 = Image.open("pictures/tv shows/Game of Thrones.jpg")
img15 = Image.open("pictures/tv shows/Seinfeld.jpg")
img16 = Image.open("pictures/tv shows/Sex and the City.jpg")
img17 = Image.open("pictures/tv shows/The Simpsons.jpg")
img18 = Image.open("pictures/tv shows/The Sopranos.jpg")
img19 = Image.open("pictures/tv shows/True Detective.jpg")

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
img20 = Image.open("pictures/actors and directors/Adrien Brody.webp")
img21 = Image.open("pictures/actors and directors/Alfred Hitchcock.webp")
img22 = Image.open("pictures/actors and directors/Christian Bale.webp")
img23 = Image.open("pictures/actors and directors/Joaquin Phoenix.webp")
img24 = Image.open("pictures/actors and directors/Johnny Depp.webp")
img25 = Image.open("pictures/actors and directors/Kate Winslet.webp")
img26 = Image.open("pictures/actors and directors/Nikolaj Coster-Waldau.webp")
img27 = Image.open("pictures/actors and directors/Quentin Tarantino.webp")
img28 = Image.open("pictures/actors and directors/Shia LaBeouf.webp")
img29 = Image.open("pictures/actors and directors/Steven Spielberg.webp")

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
img30 = Image.open("pictures/movies/Blade Runner.jpg")
img31 = Image.open("pictures/movies/Figth Club.jpg")
img32 = Image.open("pictures/movies/Forrest Gump.jpg")
img33 = Image.open("pictures/movies/Goodfellas.jpg")
img34 = Image.open("pictures/movies/Life is Beautiful.jpg")
img35 = Image.open("pictures/movies/Pulp Fiction.jpg")
img36 = Image.open("pictures/movies/Scarface.jpg")
img37 = Image.open("pictures/movies/Schindler's List.jpg")
img38 = Image.open("pictures/movies/Seven.jpg")
img39 = Image.open("pictures/movies/The Green Mile.jpg")

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