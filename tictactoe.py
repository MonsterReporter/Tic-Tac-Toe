import turtle as t
import random
t.bgcolor('#FFFFFF')
t.title("Tic Tac Toe")
#########Characters in Tic Tac Toe e.g. X's and O's###################
char1 = t.Turtle()
char2 = t.Turtle()
char3 = t.Turtle()
char4 = t.Turtle()
char5 = t.Turtle()
char6 = t.Turtle()
char7 = t.Turtle()
char8 = t.Turtle()
char9 = t.Turtle()
###################defining funcs################################
def show1():
    global starter, enimy
    if starter == "player":
        char1.hideturtle()
        char1.write("O", font=("CHALKDUSTER", 128))
        box1 = 'o'
        starter = "enemy"
        enimy.remove(char1)
        enem()
def show2():
    global starter, enimy
    if starter == "player":
        char2.hideturtle()
        char2.write("O", font=("CHALKDUSTER", 128))
        box2 = 'o'
        starter = "enemy"
        enem()
        enimy.remove(char2)
def show3():
    global starter, enimy
    if starter == "player":
        char3.hideturtle()
        char3.write("O", font=("CHALKDUSTER", 128))
        box3 = 'o'
        starter = "enemy"
        enimy.remove(char3)
        enem()
def show4():
    global starter, enimy
    if starter == "player":
        char4.hideturtle()
        char4.write("O", font=("CHALKDUSTER", 128))
        box4 = 'o'
        starter = "enemy"
        enimy.remove(char4)
        enem()
def show5():
    global starter, enimy
    if starter == "player":
        char5.hideturtle()
        char5.write("O", font=("CHALKDUSTER", 128))
        box5 = 'o'
        starter = "enemy"
        enimy.remove(char5)
        enem()
def show6():
    global starter, enimy
    if starter == "player":
        char6.hideturtle()
        char6.write("O", font=("CHALKDUSTER", 128))
        box6 = 'o'
        starter = "enemy"
        enimy.remove(char6)
        enem()
def show7():
    global starter, enimy
    if starter == "player":
        char7.hideturtle()
        char7.write("O", font=("CHALKDUSTER", 128))
        box7 = 'o'
        starter = "enemy"
        enimy.remove(char7)
        enem()
def show8():
    global starter, enimy
    if starter == "player":
        char8.hideturtle()
        char8.write("O", font=("CHALKDUSTER", 128))
        box8 = 'o'
        starter = "enemy"
        enimy.remove(char8)
        enem()
def show9():
    global starter, enimy
    if starter == "player":
        char9.hideturtle()
        char9.write("O", font=("CHALKDUSTER", 128))
        box9 = 'o'
        starter = "enemy"
        enimy.remove(char9)
        enem()
def enem():
    global enimy
    enemy = random.choice(enimy)
    if enemy == char1:
        char1.hideturtle()
        char1.write("X", font=("CHALKDUSTER", 128))
        box1 = 'x'
        enimy.remove(char1)
        starter = "player"
        loopy()
    if enemy == char2:
        char2.hideturtle()
        char2.write("X", font=("CHALKDUSTER", 128))
        box2 = 'x'
        enimy.remove(char2)
        starter = "player"
        loopy()
    if enemy == char3:
        char3.hideturtle()
        char3.write("X", font=("CHALKDUSTER", 128))
        box3 = 'x'
        enimy.remove(char3)
        starter = "player"
        loopy()
    if enemy == char4:
        char4.hideturtle()
        char4.write("X", font=("CHALKDUSTER", 128))
        box4 = 'x'
        enimy.remove(char4)
        starter = "player"
        loopy()
    if enemy == char5:
        char5.hideturtle()
        char5.write("X", font=("CHALKDUSTER", 128))
        box5 = 'x'
        enimy.remove(char5)
        starter = "player"
        loopy()
    if enemy == char6:
        char6.hideturtle()
        char6.write("X", font=("CHALKDUSTER", 128))
        box6 = 'x'
        enimy.remove(char6)
        starter = "player"
        loopy()
    if enemy == char7:
        char7.hideturtle()
        char7.write("X", font=("CHALKDUSTER", 128))
        box7 = 'x'
        enimy.remove(char7)
        starter = "player"
        loopy()
    if enemy == char8:
        char8.hideturtle()
        char8.write("X", font=("CHALKDUSTER", 128))
        box8 = 'x'
        enimy.remove(char8)
        starter = "player"
        loopy()
    if enemy == char9:
        char9.hideturtle()
        char9.write("X", font=("CHALKDUSTER", 128))
        box9 = 'x'
        enimy.remove(char9)
        starter = "player"
        loopy()
def loopy():
    global starter
    if starter == "enemy":
        starter = "player"
#############frame####################################################
line1 = t.Turtle()
line1.hideturtle()
line1.color("#AAAAAA")
line1.penup()
line1.setx(-100)
line1.sety(200)
line1.pendown()
line1.right(90)
line1.forward(400)

line2 = t.Turtle()
line2.hideturtle()
line2.color("#AAAAAA")
line2.penup()
line2.setx(100)
line2.sety(200)
line2.pendown()
line2.right(90)
line2.forward(400)

line3 = t.Turtle()
line3.hideturtle()
line3.color("#AAAAAA")
line3.penup()
line3.setx(-200)
line3.sety(100)
line3.pendown()
line3.forward(400)
line4 = t.Turtle()
line4.hideturtle()
line4.color("#AAAAAA")
line4.penup()
line4.setx(-200)
line4.sety(-100)
line4.pendown()
line4.forward(400)
#######################Variable Displays and funcs and setup#################
char1.penup()
char1.sety(120)
char1.setx(120)

char2.penup()
char2.sety(120)
char2.setx(-25)

char3.penup()
char3.sety(120)
char3.setx(-200)

char4.penup()
char4.sety(-50)
char4.setx(-200)

char5.penup()
char5.sety(-50)
char5.setx(-25)

char6.penup()
char6.sety(-50)
char6.setx(120)

char7.penup()
char7.sety(-250)
char7.setx(-200)

char8.penup()
char8.sety(-250)
char8.setx(-25)

char9.penup()
char9.sety(-250)
char9.setx(150)

box1 = ''
box2 = ''
box3 = ''
box4 = ''
box5 = ''
box6 = ''
box7 = ''
box8 = ''
box9 = ''

first = ['player', 'enemy']
enimy = [char1,char2,char3,char4,char5,char6,char7,char8,char9]
starter = random.choice(first)
############################MainLoop################################
print(" HOW TO PLAY THE GAME:")
print("")
print("")
print("press e for topright, w for topmiddle, q for topleft")
print("press a for right, s for middle, d for left")
print("press z for bottomright, x for bottommiddle, c for bottomleft")
loopy()
t.onkey(show1, "e")
t.onkey(show2, "w")
t.onkey(show3, "q")
t.onkey(show4, "a")
t.onkey(show5, "s")
t.onkey(show6, "d")
t.onkey(show7, "z")
t.onkey(show8, "x")
t.onkey(show9, "c")
t.listen()
t.mainloop()




