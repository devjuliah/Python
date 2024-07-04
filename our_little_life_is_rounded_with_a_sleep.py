from graphics import *

Window_Height = 600
Window_Width = 1000
win = GraphWin("Little Life", Window_Width, Window_Height)



#draw sword
def sword():
    myImage = Image(Point(500,250), 'Untitled_Artwork 4.gif')
    myImage.draw(win)
#draw pants
def pants():
    myImage = Image(Point(500,250), 'Untitled_Artwork.gif')
    myImage.draw(win)
#draw hallway

#draw fridge
def fridge():
#draw subconscious self (bold)
    myImage = Image(Point(500,250), 'Untitled_Artwork 8.gif')
    myImage.draw(win)
def openeye():
#draw buddy from college? self esteem queen
    myImage = Image(Point(500,250), 'Untitled_Artwork 7.gif')
    myImage.draw(win)
def benny():
    myImage = Image(Point(500,250), 'Untitled_Artwork 5.gif')
    myImage.draw(win)
def sadbenny():
#draw eyes blinking
    myImage = Image(Point(500,250), 'Untitled_Artwork 6.gif')
    myImage.draw(win)
#def eyeblink():
#    myImage = Image(Point(500,250), 'Untitled_Artwork.gif')
#    myImage.draw(win)
    
def thedoor():
    myImage = Image(Point(500,250), 'Untitled_Artwork 2.gif')
    myImage.draw(win)
def hallway():
    myImage = Image(Point(500,250), 'Untitled_Artwork 3.gif')
    myImage.draw(win)

##### Window when player is playing the game.
def playerwindow():
            #speech window
    def speechwindow():
        topleftspeechwindow = Point(100,450)
        bottomrightspeechwindow = Point(900,550)
        speechw = Rectangle(topleftspeechwindow,bottomrightspeechwindow)
        speechw.setFill("white")
        speechw.draw(win)
    speechwindow()
            #visual window
    def visualwindow():
        topleftvisualwindow = Point(100,50)
        bottomrightvisualwindow = Point(900,425)
        visualw = Rectangle(topleftvisualwindow,bottomrightvisualwindow)
        visualw.setFill("white")
        visualw.draw(win)
    visualwindow()
            #trinketswindow
    def trinketswindow():
        toplefttrinketswindow = Point(25,50)
        bottomrighttrinketswindow = Point(75,550)
        trinketsw = Rectangle(toplefttrinketswindow,bottomrighttrinketswindow)
        trinketsw.setFill("white")
        trinketsw.draw(win)
    trinketswindow()
            #health winidow
    def healthwindow():
        toplefthealthwindow = Point(925,50)
        bottomrighthealthwindow = Point(975,550)
        healthw = Rectangle(toplefthealthwindow,bottomrighthealthwindow)
        healthw.setFill("white")
        healthw.draw(win)
    healthwindow()

def healthandtrinketswindows():
    toplefttrinketswindow = Point(100,50)
    bottomrighttrinketswindow = Point(250,100)
    trinketsw = Rectangle(toplefttrinketswindow,bottomrighttrinketswindow)
    trinketsw.setFill("pink")
    trinketsw.draw(win)
    Text(Point(175,65), "Pride Levels").draw(win)

def justclotheswindow():
    toplefthealthwindow = Point(750,50)
    bottomrighthealthwindow = Point(900,100)
    healthw = Rectangle(toplefthealthwindow,bottomrighthealthwindow)
    healthw.setFill("pink")
    healthw.draw(win)
    Text(Point(825,60), "Clothes").draw(win)


#black background
def blackback():
    topleftback = Point(0,0)
    bottomrightback = Point(Window_Width, Window_Height)
    background = Rectangle(topleftback, bottomrightback)
    background.setFill("black")
    background.draw(win)
blackback()

def completeplayerwindow():
    blackback()
    playerwindow()
    healthandtrinketswindows()
    justclotheswindow()
    
def youLose():
    topleftback = Point(0,0)
    bottomrightback = Point(Window_Width, Window_Height)
    background = Rectangle(topleftback, bottomrightback)
    background.setFill("white")
    background.draw(win)
    win.getMouse()
    text = Text(Point((Window_Width/2),(Window_Height/2)),"You Lose.")
    text.draw(win)
    win.getMouse()
    win.close()
                                                #SET UP WORK
# def each window, change each click.

def startandendwindow():
    def bottomlayer():
        topleftbottomlayer = Point(50,50)
        bottomrightbottomlayer = Point(950,550)
        blw = Rectangle(topleftbottomlayer,bottomrightbottomlayer)
        blw.setFill("white")
        blw.draw(win)
    bottomlayer()
        
    def midlayer():
        topleftspeechwindow = Point(100,100)
        bottomrightspeechwindow = Point(850,500)
        speechw = Rectangle(topleftspeechwindow,bottomrightspeechwindow)
        speechw.setFill("black")
        speechw.draw(win)
    midlayer()
    
    def toplayer():
        toplefttoplayer = Point(150,150)
        bottomrighttoplayer = Point(800,450)
        tlw = Rectangle(toplefttoplayer,bottomrighttoplayer)
        tlw.setFill("white")
        tlw.draw(win)
    toplayer()
labelPoint = Point(500,300)

def instructionspeech():
    #labelPoint = Point(500,300)
    labelHome = Text(labelPoint, "Our Little Life Is Rounded With a Sleep.\n By Julia Hilker\n\nInstructions:\n\nUse your mouse to move forward.")
    labelHome.draw(win)
    win.getMouse()
    labelHome.undraw()
    
startandendwindow()
instructionspeech()


            #YOUR NAME ENTRY
whatsurname = Text(labelPoint, "What is your name?\n (click anywhere once you've entered your name)")
whatsurname.draw(win)

inputBox = Entry(Point(500,350),30)
inputBox.draw(win)
win.getMouse()
name = inputBox.getText()

while name == "":
    whatsurname.setText("Enter a name.")
    name = inputBox.getText()
    win.getMouse()
#    if name != "":
yourName = Text(Point(500, 400), "Hello, " + name)
yourName.draw(win)
win.getMouse()
inputBox.undraw()
yourName.undraw()

blackback()
playerwindow()

    # def each trinket (to be called back to later... possibly use class?
            #personal trinket: extra pieces of clothing
    
    
    #def trinket():
        

    # def health of self 

def main():
    
    def exposition():    
        def firstquotes():
            startingquotes1 = "It’s your lunch break at work. Your eyes feel very heavy, so you decide you’ll close them for just a few minutes.; You won’t fall asleep, you tell yourself. You’d never do that.; How unprofessional!; In fact, you need to make sure you’re prepared for your meeting at zzzzzzzz…"
            exquotes = startingquotes1.split(';')
            for x in exquotes:
                quotePoint = Point(500,500)
                quoteHome = Text(quotePoint, x)
                quoteHome.draw(win)
                win.getMouse()
                quoteHome.undraw()
            #win.getMouse()
            blackback()
        firstquotes()
        win.getMouse()
        playerwindow()
        def nextquotes():
            startingquotes2 = "When your eyes open, you expect to see your computer screen in front of you. Instead, you find yourself standing at the end of a long, dark hall.; At first, you feel confused. How did you get here?; Suddenly, a bright light temporarily blinds you — your gaze follows it;… and find a sword?"
            start = startingquotes2.split(';')
            for i in start:
                quotePoint2 = Point(500,500)
                quoteHome2 = Text(quotePoint2, i)
                quoteHome2.draw(win)
                win.getMouse()
                quoteHome2.undraw()
        nextquotes()
        sword()
    exposition()

    def buttons():
        textpoint = Point(500,500)
        text = Text(textpoint, "")
        text.draw(win)
        text.setText("Do you pick it up? \n(CHOOSE HERE - yes or no")
        yes = Button(win, Point(150, 500), 100, 75,'Yes')
        yes.rect.setFill("light green")
        yes.activate()

        # TO ACTIVATE BUTTON: yes.activate()

        no = Button(win, Point(850,500),100,75,"No")
        no.rect.setFill("pink")
        no.activate()

        # TO ACTIVATE BUTTON: no.activate()
        
        #left = 
        
        
        
        

        cPoint = win.getMouse()
        while True:
            if yes.clicked(cPoint):
                text.setText("Sweet! You grab it, just to -- Oh no!")
                yes.deactivate()
                no.deactivate()
                win.getMouse()
                playerwindow()
                healthandtrinketswindows()
                
                        #healthbox:
                
                initialhealth = float(100)
                health = Text(Point(175,80), initialhealth)
                health.draw(win)
                
                
                justclotheswindow()
                
                
                initialclothes = float(0.0)
                clothes = Text(Point(825, 75), initialclothes)
                clothes.draw(win)
                hallway()
                def movingon():    
                    startingquotes = "You cut yourself with your new sword. That's when you realize you aren't wearing clothes. How embarrassing!;You're giving a presentation in half an hour. You can't go on like this!;You're lose 50% of your pride."
                    exquotes = startingquotes.split(';')
                    for x in exquotes:
                        quotePoint = Point(500,500)
                        quoteHome = Text(quotePoint, x)
                        quoteHome.draw(win)
                        win.getMouse()
                        quoteHome.undraw()
                    #healthbox()
                    #win.getMouse()
                movingon()
                newpride = float(initialhealth - 50)
                newhealth = health.setText(newpride)           
                
                def youneedclothes():
                    nextquotes = "\nYou need clothes... \nASAP.;Maybe you'll find clothes down that hallway?"
                    iquotes = nextquotes.split(';')
                    for i in iquotes:
                        quoteP = Point(500,500)
                        quoteH = Text(quoteP, i)
                        quoteH.draw(win)
                        win.getMouse()
                        quoteH.undraw()
                    #win.getMouse()
                
                #heal.draw(win)
                youneedclothes()
                
                def downthehall():
                    startingquotes = "Littered through the hall, you see random articles of clothing you can pick up.;But not just that... At the end of the hall, you see the most important piece of all: pants!;hanging from a perfectly lit statute, as if they're waiting just for you. It's your lucky day!;Unfortunately, you see three doors you'll have to pass through before you're late for your meeting...;And who knows what obstacles you'll come face to face with.;You have a new goal: reach the end of the hall without dying of embarrassment\n(and getting as many pieces of clothing as you can)."
                    exquotes = startingquotes.split(';')
                    for x in exquotes:
                        quotePoint = Point(500,500)
                        quoteHome = Text(quotePoint, x)
                        quoteHome.draw(win)
                        win.getMouse()
                        quoteHome.undraw()
                downthehall()
                pants()


                #how many steps should you take forward (1-10)?
                    # if 8 or less, then you have to face enemy one. At the end, you can get +2 articles of clothing (from off him.. socks, shoes, and a tshirt)
                    # if 9 or more, you missed enemy one -- did you see benny in there? well, maybe it's best you didn't see him. (you pick up one pair of shoes. you put them on; your feet stinky... you gain +1 trinket)
                    #if 0 steps, your old high school bully (enemy one) leaves the room and laughs at you. you lose 50% embarrrarssment. 
                    
                def stepsforward():
                    stepspoint = Point(500,500)
                    stepstext = Text(stepspoint,"Out of 10, how many steps do you want to take?")
                    stepstext.draw(win)
                    inputBox = Entry(Point(500,350),30)
                    inputBox.draw(win)
                    win.getMouse()
                    usersteps = inputBox.getText()
                    while usersteps == "":
                        stepstext.setText("Enter a whole number between 1 and 10")
                        usersteps = inputBox.getText()
                        win.getMouse()
                    #stepstext.setText("you chose to move forward " + usersteps + " steps!")
                    win.getMouse()
                    usersteps = int(usersteps)

                    if (usersteps >= 1 and usersteps <= 10):
                        inputBox.undraw()
                        stepstext.setText("Great!")
                        win.getMouse()
                        stepstext.setText(" ")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                            ## ENEMY NUMBER ONE!!!

                        if usersteps < 9:
                            def lessthan9():
                                stepstext9 = ("You move forward. Unfortunately, you stop right in front of an open door;--and come face to face with your high school bully...")
                                exquotes = stepstext9.split(';')
                                for x in exquotes:
                                    quotePoint = Point(500,500)
                                    quoteHome = Text(quotePoint, x)
                                    quoteHome.draw(win)
                                    win.getMouse()
                                    quoteHome.undraw()
                            lessthan9()
                            benny()
                            #insert the semicolon thing here.
                            #INSERRT PICTURE OF BENNY HERE. he's ugly af. just so you know. 
                            def nextinline():
                                newnextinline = ("Benny; God, Benny. He hasn't changed a bit. Still handsome. Still cool.;Just look at him.; You try to walk away, but suddenly, he points at you and laughs. Laughs!; You feel frozen in the memories of your high-school self, standing there as he laughs at you. Your pride goes down 20 points.")
                                #inserrt semicolon thing here.
                                exquotes = newnextinline.split(';')
                                for x in exquotes:
                                    quotePoint = Point(500,500)
                                    quoteHome = Text(quotePoint, x)
                                    quoteHome.draw(win)
                                    win.getMouse()
                                    quoteHome.undraw()
                            nextinline()
                            stepstext.setText("You're frozen.")
                            
                            bullypridedown = float(newpride - 20)
                            bullyhealth1 = health.setText(bullypridedown)
                            #bullyhealth.draw()
                            
                            #you look around - that voice didn't come from you, did it? 
                            yoursubconsciouspoint = Point(500, 400)
                            yoursubconscious = ("Are you just going to stand around and take this?; Let him laugh at you?; Or are you going to stand up for yourself, and take back your power?")
                            splitsubconscious = yoursubconscious.split(';')
                            for x in splitsubconscious:
                                quotePoint = Text(yoursubconsciouspoint, x)
                                quotePoint.setStyle("bold italic")
                                quotePoint.draw(win)
                                win.getMouse()
                                quotePoint.undraw()
                            stepstext.setText(" ")
                            
        
                            huh = ("You look around, confused;That voice didn't come from you, did it?;You shake your head, shaking it off.;You look back at Benny.")
                            stepsextext = huh.split(';')
                            for x in stepsextext:
                                ohpoint = Point(500,500)
                                ohquoteHome = Text(ohpoint, x)
                                ohquoteHome.draw(win)
                                win.getMouse()
                                ohquoteHome.undraw()
                            
                               
                    
                            text.setText("What do you do?")
                            #clickerpoint = win.getMouse()
                            #def bigdecision():
                            #while True:
                            def bigdecision():
                                
                                standbutton = Button(win, Point(150, 500), 100, 75,'Fight.')
                                standbutton.rect.setFill("light green")
                                standbutton.activate()

                                runbutton = Button(win, Point(850, 500), 100, 75,'Run.')
                                runbutton.rect.setFill("red")
                                runbutton.activate()
                                
                                clickerpoint = win.getMouse()   
                        
                                text.setText("What do you do?")
                                
                                
                                if runbutton.clicked(clickerpoint):
                                    runbutton.deactivate()
                                    standbutton.deactivate()
                                    clothes.undraw()
                                    health.undraw()
                                    playerwindow()
                                    healthandtrinketswindows()
                                    justclotheswindow()
                                    clothes.draw(win)
                                    health.draw(win)
                                    clothesupdate = float(initialclothes + 0)
                                    clothesupdatedraw = clothes.setText(clothesupdate)
                                    #clothesupdatedraw.draw(win)
                                    bulliedtodeath = float(30 - 30)
                                    bulliedhealth = health.setText(bulliedtodeath)
                                    #bulliedhealth.draw(win)
                                    runtext = "You run away, crying, your pride reaching zero.;You've died of embarrassment.;You deserved better for yourself.;Maybe in the next dream, you'll find the strength to fight for yourself...;You wake up, feeling unprepared for your meeting."
                                    runquote = runtext.split(';')
                                    for x in runquote:
                                        runquotePoint = Point(500,500)
                                        runquoteHome = Text(runquotePoint, x)
                                        runquoteHome.draw(win)
                                        win.getMouse()
                                        runquoteHome.undraw()
                     
                                    youLose()
                                    
                                    
                                    
                                    
                                elif standbutton.clicked(clickerpoint):
                                    runbutton.deactivate()
                                    standbutton.deactivate()
                                    clothes.undraw()
                                    health.undraw()
                                    playerwindow()
                                    healthandtrinketswindows()
                                    justclotheswindow()
                                    clothes.draw(win)
                                    health.draw(win)
                                    
                                    #completeplayerwindow()
                                    #bulliedtodeath1 = float(bullypridedown - 0)
                                    #bulliedhealth1 = health.setText(bulliedtodeath1)
                                    #bulliedhealth1.draw(win)
                                    #clothes.undraw()
                                    #clothesupdate = float(initialclothes + 0)
                                    #clothesupdatedraw = clothes.setText(clothesupdate)
                                    #clothesupdatedraw.draw(win)
                                    #bulliedtodeath = float(bullypridedown - 30)
                                    sadbenny()
                                    newtext = ("Benny is shocked.;He falls from the shock, knocking his head in the process, not moving.;For a moment, you panic...\nBut his chest is rising.;You decide stealing from someone who isn't dead is okay, and you get some of his clothes from him.;Awesome!\nNow, you have socks AND shoes, gaining +2 clothes...;And, because you stood up for yourself, you gain +20 pride.")
                                    newtexts = Text(Point(500,500),newtext)
                                    fightquote = newtext.split(';')
                                    for x in fightquote:
                                        fightquotePoint = Point(500,500)
                                        fightquoteHome = Text(fightquotePoint, x)
                                        fightquoteHome.draw(win)
                                        win.getMouse()
                                        fightquoteHome.undraw()
                                    #newtexts.draw(win)
                                    
                                    
                                    newerclothes = float(initialclothes + 2)
                                    newerclothesdraw = clothes.setText(newerclothes)
                                    #win.getMouse()
                                    newtexts.undraw()
                                    bulliedtodeath2 = float(30 + 20)
                                    bulliedhealth1 = health.setText(bulliedtodeath2)
                                    #newtexts.setText("You continue forward.;How many steps should you take?")
                                    
                                    def secondlevelsteps():
                                        
                                        stepspoint1 = Point(500,500)
                                        stepstext2 = Text(stepspoint1,"You continue forward.")
                                        stepstext2.draw(win)
                                        #inputBox2 = Entry(Point(500,350),30)
                                        #inputBox2.draw(win)
                                        #win.getMouse()
                                        #usersteps2 = inputBox2.getText()
                                        #while usersteps2 == "":
                                       #     stepstext2.setText("Enter a whole number between 1 and 10")
                                       #     usersteps2 = inputBox2.getText()
                                       #     win.getMouse()
                                        #stepstext2.setText("you chose to move forward " + usersteps2 + " steps!")
                                        #win.getMouse()
                                        #usersteps2 = int(usersteps2)

                                        #if (usersteps2 >= 1 and usersteps2 <= 10):
                                        #    inputBox2.undraw()
                                        #    stepstext2.setText("You move on.")
                                        #    win.getMouse()
                                        
                                        #stepstext2.setText(" ")
                                    #secondlevelsteps()
                                                                                ## ENEMY NUMBER TWO - the FRIDGE

                         
                                    fridge()
                                    def lessthan92():
                                        stepstext29 = ("At the next door you reach, you see a fridge.;You're not hungry, but what could getting a little food hurt?;A lot, apparrently.;Right before you open the fridge,it opens by itself,\na large mouth-like opening, as the fridge starts speaking.")
                                        exquotes = stepstext29.split(';')
                                        for x in exquotes:
                                            quotePoint = Point(500,500)
                                            quoteHome = Text(quotePoint, x)
                                            quoteHome.draw(win)
                                            win.getMouse()
                                            quoteHome.undraw()
                                        
                                    lessthan92()

                                    #INSERRT PICTURE OF THE FRIDGEEE 
                                    def nextinline2():
                                        newnextinline2 = ("'Aha!' he says. 'I have enticed you with my power!; Before you continue, you must eat a food from within me.'")
                                        #inserrt semicolon thing here.
                                        exquotes = newnextinline2.split(';')
                                        for x in exquotes:
                                            quotePoint = Point(500,500)
                                            quoteHome = Text(quotePoint, x)
                                            quoteHome.draw(win)
                                            win.getMouse()
                                            quoteHome.undraw()
                                    nextinline2()
                                    
                                    #stepstext2.setText("What do you choose?")
                                    
                                    #clothesupdate = float(newerclothes)
                                    #clothesupdatedraw = clothes.setText()
                                    #bulliedtodeath = float(bulliedtodeath2)
                                    #bulliedhealth = health.setText(bulliedtodeath)
                                    def imwaiting():
                                        subconscioustext29 = ("Stay away from the fridge;Food is bad for you;Walk away.")
                                        exquotes123 = subconscioustext29.split(';')
                                        for x in exquotes123:
                                            quotePoint1 = Point(500,400)
                                            quoteHome1 = Text(quotePoint1, x)
                                            quoteHome1.setStyle("bold italic")
                                            quoteHome1.draw(win)
                                            win.getMouse()
                                            quoteHome1.undraw()
                                        imwaiting = "'I'm waiting,' the fridge says."
                                        quotePointw = Point(500,500)
                                        quoteHomew = Text(quotePointw, imwaiting)
                                        quoteHomew.draw(win)
                                        win.getMouse()
                                        quoteHomew.undraw()
                                    imwaiting()
                                    
                                    def fridgedecisions():
                                        eatbutton = Button(win, Point(150, 500), 100, 75,'Eat Food.')
                                        eatbutton.rect.setFill("light green")
                                        eatbutton.activate()

                                        stabbutton = Button(win, Point(850, 500), 100, 75,'Stab It')
                                        stabbutton.rect.setFill("red")
                                        stabbutton.activate()
                                        
                                        clickerpoint = win.getMouse()   
                                
                                        text.setText("What do you do?")
                                        while True:
#________________________________________________________________________________________________________________________________________________________________________________________________
                                            if stabbutton.clicked(clickerpoint):
                                                stabbutton.deactivate()
                                                eatbutton.deactivate()
                                                completeplayerwindow()
                                                clothes.undraw()
                                                health.undraw()
                                                #playerwindow()
                                                healthandtrinketswindows()
                                                justclotheswindow()
                                                clothes.draw(win)
                                                health.draw(win)
                                                newerclothes = float(initialclothes + 4)
                                                newerclothesdraw = clothes.setText(newerclothes)
                                                #win.getMouse()
                                                bulliedtodeath2 = float(30 + 20)
                                                bulliedhealth1 = health.setText(bulliedtodeath2)
                                                #bulliedhealth1.draw(win)
                                                
                                                
                                                
                                                def runningtext():
                                                    runtext = "You stab the fridge with your sword.;With a cry, it says, 'I provide you with comfort when you're sad. Why would you hurt me?';It sparks, and lets out a little puff of air, going dark.;You feel guilty, but you can't think about it too long.\nYour meeting is soon.;Instead, you open the fridge and see a t-shirt, covered in icecreram?; You pull it out, and the icecream melts, so you pull it over your head, shivering from the cold fabric.;Though it's sticky, you smell good now.;You gain +1 clothing and gain +20 pride"
                                                    runquote = runtext.split(';')
                                                    for x in runquote:
                                                        runquotePoint = Point(500,500)
                                                        runquoteHome = Text(runquotePoint, x)
                                                        runquoteHome.draw(win)
                                                        win.getMouse()
                                                        runquoteHome.undraw()
                                                runningtext()
                                 
                                                #youLose()
                                                #win.getMouse()
                                                clothesupdate3 = float(newerclothes + 1)
                                                clothesupdate4 = clothes.setText(clothesupdate3)
                                                #clothesupdateraw3.draw(win)
                                                bulliedtodeath3 = float(bulliedtodeath2 +20 )
                                                bulliedhealth3 = health.setText(bulliedtodeath3)
                                                #bulliedhealth2.draw(win)
                                                
                                                
                                                movingonbabypoint = Point(500,500)
                                                movingonbaby = Text(movingonbabypoint, "You continue forward...")
                                                movingonbaby.draw(win)
                                                win.getMouse()
                                                thedoor()
                                                movingonbaby.setText("They're right there. The pants.")
                                                win.getMouse()
                                                movingonbaby.setText("But just as you're about to open, the door...")
                                                win.getMouse()
                                                movingonbaby.setText("the lights go out.")
                                                win.getMouse()
                                                
                                                                                    ##########
                                                                                    #ENEMY 3
                                                
                                                def subconsciousenemy3():
            #PICTURE OF THE EYES OPENING.
                                                
                                                #subconscioustextenemy3 = (" blah .")
                                                #exquotessub = subconscioustextenemy3.split(';')
                                                #for x in exquotessub:
                                               #     quotePoint1 = Point(500,400)
                                               #     quoteHome1 = Text(quotePoint1, x)
                                               #     quoteHome1.setStyle("bold italic")
                                               #     quoteHome1.draw(win)
                                               #     win.getMouse()
                                               #     quoteHome1.undraw()
                                                
                                                    def convo():
                                                        blackback()
                                                        
                                                        
                                                        #leave on eyes open
                                                        
                                                        
                                                        
                                                        subtopleftback = Point(200,375)
                                                        subbottomrightback = Point(800,420)
                                                        subbackground = Rectangle(subtopleftback, subbottomrightback)
                                                        subbackground.setFill("grey")
                                                        subbackground.draw(win)
                                                        
                                                        selftopleftback = Point(200,475)
                                                        selfbottomrightback = Point(800,520)
                                                        selfbackground = Rectangle(selftopleftback, selfbottomrightback)
                                                        selfbackground.setFill("white")
                                                        selfbackground.draw(win)
                                                        
                                                        
                                                        #set up textbox and text for self
                                                        subconsciousconvoPoint = Point(500,400)
                                                        subconsciousconvo = Text(subconsciousconvoPoint,"hello")
                                                        subconsciousconvo.setStyle("bold italic")
                                                        subconsciousconvo.draw(win)
                                                        win.getMouse()
                                                        subconsciousconvo.undraw()
                                                        
                                                        #set up textbok and text for subconscious
                                                        selfconvoPoint = Point(500,500)
                                                        selfconvo = Text(selfconvoPoint,"hello? who are you?")
                                                        selfconvo.setStyle("bold italic")
                                                        #selfconvobox = rectangle
                                                        selfconvo.draw(win)
                                                        win.getMouse()
                                                        selfconvo.undraw()
                                                        
                                                        subconsciousconvo.setText("i am you")
                                                        subconsciousconvo.draw(win)
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("but i'm me")
                                                        selfconvo.draw(win)
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("true... \ni'm the you that you don't want to see. both your dreams and your nightmares. \nyou're afraid of your truths, you know.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("that's confusing. i just need pants so i can get to my meeting on time.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("the pants are all you see.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("they're glowing yellow in this black and white dream. \nyes, they're all i can see.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("what do you think the pants could represent?")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("i dunno... you tell me.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("that's not my job. i'm just here to call attention to them.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("this is dumb. let me wake up.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("i don't know. i think there's more about yourself you should pay attention to.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("can i get the pants first?")
                                                        win.getMouse()
                                                        
                                                        
                                                        
                                                        
                                #eyes blink.
                                                        
                                                        
                                                        
                                                        subconsciousconvo.setText("will you pay attention to your dreams more?")
                                                        win.getMouse()
                                                        
                                                        
                                                        
                                                        
                                                        listening = Button(win, Point(150, 500), 100, 75,'Promise to\nListen')
                                                        listening.rect.setFill("white")
                                                        listening.activate()

                                                        ignoring = Button(win, Point(850, 500), 100, 75,'Ignore')
                                                        ignoring.rect.setFill("white")
                                                        ignoring.activate()
                                                        
                                                        clickerpoints = win.getMouse()   
                                                
                                                        text.setText("What do you do?")
                                                        
                                                        while True:
                                                            if listening.clicked(clickerpoints):
                                    #eyes blink closed.
                                                                listening.deactivate()
                                                                ignoring.deactivate()
                                                                blackback()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                subbackground.draw(win)
                                                                #selfbackground.draw(win)
                                                                subconsciousconvo.draw(win)
                                                                #selfconvo.draw(win)
                                                                
                                                                clothesupdate4 = float(5 + 1)
                                                                clothesupdate4 = str(clothesupdate4)
                                                                bulliedtodeath4 = float(bulliedtodeath2 + 50)
                                                                bulliedtodeath4 = str(bulliedtodeath4)
                                                                
                                                                subconsciousconvo.setText("thank you. here are your pants...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("before you wake up, know you also gained 30 pride.\nyour final scores were...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("Clothes: " + clothesupdate4 + "Pride:" + bulliedtodeath4)
                                                                win.getMouse()
                                                                startandendwindow()
                                                                #you  wake up, feleing well rrested, and sstart searching for another job,
                                                                #or at least a hobby.
                                                                yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                                yourName.draw(win)
                                                                win.getMouse()
                                                                yourName.undraw()
                                                                def endwords():
                                                                    runtext = ("You conduct a fantastic meeting.;However, once you're done, you start looking for a new job.;Maybe things will start to make sense.")
                                                                    runquote = runtext.split(';')
                                                                    for x in runquote:
                                                                        runquotePoint = Point(500,300)
                                                                        runquoteHome = Text(runquotePoint, x)
                                                                        runquoteHome.draw(win)
                                                                        win.getMouse()
                                                                        runquoteHome.undraw()
                                                                endwords()
                                                                #inputBox.undraw()
                                                                #yourName.undraw()
                                                                blackback()
                                                                win.close()
                                                            
                                                            elif ignoring.clicked(clickerpoints):
                                                                
                                                                blackback()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                subbackground.draw(win)
                                                                #selfbackground.draw(win)
                                                                subconsciousconvo.draw(win)
                                                                #selfconvo.draw(win)
                                                                
                                                                clothesupdate4 = float(5)
                                                                clothesupdate4 = str(clothesupdate4)
                                                                bulliedtodeath4 = float(bulliedtodeath2)
                                                                bulliedtodeath4 = str(bulliedtodeath4)
                                                                
                                                                listening.deactivate()
                                                                ignoring.deactivate()
                                                                
                                                
                                                                subconsciousconvo.setText("im sorry. i hope you learn to listen better")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("before you wake up, your final scores were...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("Clothes: " + clothesupdate4 + ", Pride: " + bulliedtodeath4)
                                                                #i'm sorry. hopefully with time you learn to listen better.
            
                                                                win.getMouse()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                #
                                                                startandendwindow()
                                                                
    
                                                                
                                                                yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                                yourName.draw(win)
                                                                win.getMouse()
                                                                yourName.undraw()
                                                                
                                                                def endwords():
                                                                    runtext = "Guess you gotta get back to work;hopefully you don't fall asleep;Also, just one more thing...;You're not wearing pants."
                                                                    runquote = runtext.split(';')
                                                                    for x in runquote:
                                                                        runquotePoint = Point(500,300)
                                                                        runquoteHome = Text(runquotePoint, x)
                                                                        runquoteHome.draw(win)
                                                                        win.getMouse()
                                                                        runquoteHome.undraw()
                                                                endwords()
                                                                
                                                                blackback()
                                                                win.close()
                                                                #you wake up, disoriented, getting ready for the meeting you hate.
                                                                #what a weird dream.
                                                                #end game.
                                                                
                                                    convo()
                                                
                                                subconsciousenemy3()
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                
###_________________________________________________________________________________________________________________________________________________________________________________________________
                                            
                                            elif eatbutton.clicked(clickerpoint):
                                                
                                                stabbutton.deactivate()
                                                eatbutton.deactivate()
                                                completeplayerwindow()
                                                clothes.undraw()
                                                health.undraw()
                                                #playerwindow()
                                                healthandtrinketswindows()
                                                justclotheswindow()
                                                clothes.draw(win)
                                                health.draw(win)
                                                newerclothes = float(initialclothes + 4)
                                                newerclothesdraw = clothes.setText(newerclothes)
                                                #win.getMouse()
                                                bulliedtodeath2 = float(30 + 20)
                                                #health.draw(win)
                                                bulliedhealth1 = health.setText(bulliedtodeath2)
                                                
                                                #bulliedhealth1.draw(win)
                                                
                                                def eatruntext():
                                                    runtext = ("You grab the offered a cup of icecreram;It's delicious, but you also quickly learn, as you bite on it, there's a t-shirt inside;The fridge starts laughing at you at his prank.\nThe fact you fell for something so stupid makes you lose -10 pride.;Still, you got a shirt out of it, so you put it on and move on\nwaving to the laughing fridge on the way out.")
                                                    runquote = runtext.split(';')
                                                    for x in runquote:
                                                        runquotePoint = Point(500,500)
                                                        runquoteHome = Text(runquotePoint, x)
                                                        runquoteHome.draw(win)
                                                        win.getMouse()
                                                        runquoteHome.undraw()
                                                    #win.getMouse()
                                                    
                                                    
                                                    
                                                eatruntext()
                                 
                                                #youLose()
                                                clothesupdate3 = float(newerclothes + 1)
                                                clothesupdate4 = clothes.setText(clothesupdate3)
                                                #clothesupdateraw3.draw(win)
                                                bulliedtodeath3 = float(bulliedtodeath2 -10 )
                                                bulliedhealth3 = health.setText(bulliedtodeath3)
                                                
                                                win.getMouse()
                                                movingonbabypoint = Point(500,500)
                                                movingonbaby = Text(movingonbabypoint, "You continue forward...")
                                                movingonbaby.draw(win)
                                                win.getMouse()
                                                thedoor()
                                                movingonbaby.setText("They're right there. The pants.")
                                                win.getMouse()
                                                movingonbaby.setText("But just as you're about to open, the door...")
                                                win.getMouse()
                                                movingonbaby.setText("the lights go out.")
                                                win.getMouse()
                                                     
                                                
                                                
                                                                    ###### ENEMY THRREE BABY (COPY IT OVERR!!
                                                
                                                
                                                                           
                                                def subconsciousenemy3():
            #PICTURE OF THE EYES OPENING.
                                                
                                                #subconscioustextenemy3 = (" blah .")
                                                #exquotessub = subconscioustextenemy3.split(';')
                                                #for x in exquotessub:
                                               #     quotePoint1 = Point(500,400)
                                               #     quoteHome1 = Text(quotePoint1, x)
                                               #     quoteHome1.setStyle("bold italic")
                                               #     quoteHome1.draw(win)
                                               #     win.getMouse()
                                               #     quoteHome1.undraw()
                                                
                                                    def convo():
                                                        blackback()
                                                        
                                                        
                                                        #leave on eyes open
                                                        
                                                        
                                                        
                                                        subtopleftback = Point(200,375)
                                                        subbottomrightback = Point(800,420)
                                                        subbackground = Rectangle(subtopleftback, subbottomrightback)
                                                        subbackground.setFill("grey")
                                                        subbackground.draw(win)
                                                        
                                                        selftopleftback = Point(200,475)
                                                        selfbottomrightback = Point(800,520)
                                                        selfbackground = Rectangle(selftopleftback, selfbottomrightback)
                                                        selfbackground.setFill("white")
                                                        selfbackground.draw(win)
                                                        
                                                        
                                                        #set up textbox and text for self
                                                        subconsciousconvoPoint = Point(500,400)
                                                        subconsciousconvo = Text(subconsciousconvoPoint,"hello")
                                                        subconsciousconvo.setStyle("bold italic")
                                                        subconsciousconvo.draw(win)
                                                        win.getMouse()
                                                        subconsciousconvo.undraw()
                                                        
                                                        #set up textbok and text for subconscious
                                                        selfconvoPoint = Point(500,500)
                                                        selfconvo = Text(selfconvoPoint,"hello? who are you?")
                                                        selfconvo.setStyle("bold italic")
                                                        #selfconvobox = rectangle
                                                        selfconvo.draw(win)
                                                        win.getMouse()
                                                        selfconvo.undraw()
                                                        
                                                        subconsciousconvo.setText("i am you")
                                                        subconsciousconvo.draw(win)
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("but i'm me")
                                                        selfconvo.draw(win)
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("true... \ni'm the you that you don't want to see. both your dreams and your nightmares. \nyou're afraid of your truths, you know.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("that's confusing. i just need pants so i can get to my meeting on time.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("the pants are all you see.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("they're glowing yellow in this black and white dream. \nyes, they're all i can see.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("what do you think the pants could represent?")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("i dunno... you tell me.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("that's not my job. i'm just here to call attention to them.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("this is dumb. let me wake up.")
                                                        win.getMouse()
                                                        
                                                        subconsciousconvo.setText("i don't know. i think there's more about yourself you should pay attention to.")
                                                        win.getMouse()
                                                        
                                                        selfconvo.setText("can i get the pants first?")
                                                        win.getMouse()
                                                        
                                                        
                                                        
                                                        
                                #eyes blink.
                                                        
                                                        
                                                        
                                                        subconsciousconvo.setText("will you pay attention to your dreams more?")
                                                        win.getMouse()
                                                        
                                                        
                                                        
                                                        
                                                        listening = Button(win, Point(150, 500), 100, 75,'Promise to\nListen')
                                                        listening.rect.setFill("white")
                                                        listening.activate()

                                                        ignoring = Button(win, Point(850, 500), 100, 75,'Ignore')
                                                        ignoring.rect.setFill("white")
                                                        ignoring.activate()
                                                        
                                                        clickerpoints = win.getMouse()   
                                                
                                                        text.setText("What do you do?")
                                                        
                                                        while True:
                                                            if listening.clicked(clickerpoints):
                                    #eyes blink closed.
                                                                listening.deactivate()
                                                                ignoring.deactivate()
                                                                blackback()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                subbackground.draw(win)
                                                                #selfbackground.draw(win)
                                                                subconsciousconvo.draw(win)
                                                                #selfconvo.draw(win)
                                                                
                                                                clothesupdate4 = float(5 + 1)
                                                                clothesupdate4 = str(clothesupdate4)
                                                                bulliedtodeath4 = float(bulliedtodeath2 + 50)
                                                                bulliedtodeath4 = str(bulliedtodeath4)
                                                                
                                                                subconsciousconvo.setText("thank you. here are your pants...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("before you wake up, know you also gained 30 pride.\nyour final scores were...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("Clothes: " + clothesupdate4 + "Pride:" + bulliedtodeath4)
                                                                win.getMouse()
                                                                startandendwindow()
                                                                #you  wake up, feleing well rrested, and sstart searching for another job,
                                                                #or at least a hobby.
                                                                yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                                yourName.draw(win)
                                                                win.getMouse()
                                                                yourName.undraw()
                                                                def endwords():
                                                                    runtext = ("You conduct a fantastic meeting.;However, once you're done, you start looking for a new job.;Maybe things will start to make sense.")
                                                                    runquote = runtext.split(';')
                                                                    for x in runquote:
                                                                        runquotePoint = Point(500,300)
                                                                        runquoteHome = Text(runquotePoint, x)
                                                                        runquoteHome.draw(win)
                                                                        win.getMouse()
                                                                        runquoteHome.undraw()
                                                                endwords()
                                                                #inputBox.undraw()
                                                                #yourName.undraw()
                                                                blackback()
                                                                win.close()
                                                            
                                                            elif ignoring.clicked(clickerpoints):
                                                                
                                                                blackback()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                subbackground.draw(win)
                                                                #selfbackground.draw(win)
                                                                subconsciousconvo.draw(win)
                                                                #selfconvo.draw(win)
                                                                
                                                                clothesupdate4 = float(5)
                                                                clothesupdate4 = str(clothesupdate4)
                                                                bulliedtodeath4 = float(bulliedtodeath2)
                                                                bulliedtodeath4 = str(bulliedtodeath4)
                                                                
                                                                listening.deactivate()
                                                                ignoring.deactivate()
                                                                
                                                
                                                                subconsciousconvo.setText("im sorry. i hope you learn to listen better")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("before you wake up, your final scores were...")
                                                                win.getMouse()
                                                                subconsciousconvo.setText("Clothes: " + clothesupdate4 + ", Pride: " + bulliedtodeath4)
                                                                #i'm sorry. hopefully with time you learn to listen better.
            
                                                                win.getMouse()
                                                                subbackground.undraw()
                                                                selfbackground.undraw()
                                                                subconsciousconvo.undraw()
                                                                selfconvo.undraw()
                                                                #
                                                                startandendwindow()
                                                                

                                                                
                                                                yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                                yourName.draw(win)
                                                                win.getMouse()
                                                                yourName.undraw()
                                                                
                                                                def endwords():
                                                                    runtext = "Guess you gotta get back to work;hopefully you don't fall asleep;Also, just one more thing...;You're not wearing pants."
                                                                    runquote = runtext.split(';')
                                                                    for x in runquote:
                                                                        runquotePoint = Point(500,300)
                                                                        runquoteHome = Text(runquotePoint, x)
                                                                        runquoteHome.draw(win)
                                                                        win.getMouse()
                                                                        runquoteHome.undraw()
                                                                endwords()
                                                                
                                                                blackback()
                                                                win.close()
                                                                #you wake up, disoriented, getting ready for the meeting you hate.
                                                                #what a weird dream.
                                                                #end game.
                                                                
                                                    convo()
                                                
                                                subconsciousenemy3()
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                            else:
                                                
                                                frnewtext = ("Make a choice.")
                                                frnewtexts = Text(Point(500,500), frnewtext)
                                                frnewtexts.draw(win)
                                                win.getMouse()
                                                frnewtexts.setText(" ")
                                                fridgedecisions()
                                    fridgedecisions()
                                        
                                
                                    #secondlevelsteps()

                                        
                                    
                                #elif not runbutton.clicked(clickerpoint) or standbutton.clicked(clickerpoint):
                                else:
                                    
                                    frnewtext = ("Make a choice.")
                                    frnewtexts = Text(Point(500,500), frnewtext)
                                    frnewtexts.draw(win)
                                    win.getMouse()
                                    frnewtexts.setText(" ")
                                    bigdecision()
                            bigdecision()
                                
                                #nextinline()
                                #frnewtext.setText(" ")                                    
                      
                                
                                #bigdecision()
                                    
                            #bigdecision()
                                
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                
                                        
                                
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                                
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
                                        
    
                                    ##moving on i gUESS
                        elif usersteps >= 9:
                            def morethan9():
                        
                                fridge()
                                def lessthan92():
                                    stepstext29 = ("At the next door you reach, you see a fridge.;You're not hungry, but what could getting a little food hurt?;A lot, apparrently.;Right before you open the fridge,it opens by itself,\na large mouth-like opening, as the fridge starts speaking.")
                                    exquotes = stepstext29.split(';')
                                    for x in exquotes:
                                        quotePoint = Point(500,500)
                                        quoteHome = Text(quotePoint, x)
                                        quoteHome.draw(win)
                                        win.getMouse()
                                        quoteHome.undraw()
                                    
                                lessthan92()

                                #INSERRT PICTURE OF THE FRIDGEEE 
                                def nextinline2():
                                    newnextinline2 = ("'Aha!' he says. 'I have enticed you with my power!; Before you continue, you must eat a food from within me.'")
                                    #inserrt semicolon thing here.
                                    exquotes = newnextinline2.split(';')
                                    for x in exquotes:
                                        quotePoint = Point(500,500)
                                        quoteHome = Text(quotePoint, x)
                                        quoteHome.draw(win)
                                        win.getMouse()
                                        quoteHome.undraw()
                                nextinline2()
                                
                                #stepstext2.setText("What do you choose?")
                                
                                #clothesupdate = float(newerclothes)
                                #clothesupdatedraw = clothes.setText()
                                #bulliedtodeath = float(bulliedtodeath2)
                                #bulliedhealth = health.setText(bulliedtodeath)
                                def imwaiting():
                                    subconscioustext29 = ("Stay away from the fridge;Food is bad for you;Walk away.")
                                    exquotes123 = subconscioustext29.split(';')
                                    for x in exquotes123:
                                        quotePoint1 = Point(500,400)
                                        quoteHome1 = Text(quotePoint1, x)
                                        quoteHome1.setStyle("bold italic")
                                        quoteHome1.draw(win)
                                        win.getMouse()
                                        quoteHome1.undraw()
                                    imwaiting = "'I'm waiting,' the fridge says."
                                    quotePointw = Point(500,500)
                                    quoteHomew = Text(quotePointw, imwaiting)
                                    quoteHomew.draw(win)
                                    win.getMouse()
                                    quoteHomew.undraw()
                                imwaiting()
                                
                                def fridgedecisions():
                                    eatbutton = Button(win, Point(150, 500), 100, 75,'Eat Food.')
                                    eatbutton.rect.setFill("light green")
                                    eatbutton.activate()

                                    stabbutton = Button(win, Point(850, 500), 100, 75,'Stab It')
                                    stabbutton.rect.setFill("red")
                                    stabbutton.activate()
                                    
                                    clickerpoint = win.getMouse()   
                            
                                    text.setText("What do you do?")
                                    while True:
    #________________________________________________________________________________________________________________________________________________________________________________________________
                                        if stabbutton.clicked(clickerpoint):
                                            stabbutton.deactivate()
                                            eatbutton.deactivate()
                                            completeplayerwindow()
                                            clothes.undraw()
                                            health.undraw()
                                            #playerwindow()
                                            healthandtrinketswindows()
                                            justclotheswindow()
                                            clothes.draw(win)
                                            health.draw(win)
                                            newerclothes = float(initialclothes + 4)
                                            newerclothesdraw = clothes.setText(newerclothes)
                                            #win.getMouse()
                                            bulliedtodeath2 = float(30 + 20)
                                            bulliedhealth1 = health.setText(bulliedtodeath2)
                                            #bulliedhealth1.draw(win)
                                            
                                            
                                            
                                            def runningtext():
                                                runtext = "You stab the fridge with your sword.;With a cry, it says, 'I provide you with comfort when you're sad. Why would you hurt me?';It sparks, and lets out a little puff of air, going dark.;You feel guilty, but you can't think about it too long.\nYour meeting is soon.;Instead, you open the fridge and see a t-shirt, covered in icecreram?; You pull it out, and the icecream melts, so you pull it over your head, shivering from the cold fabric.;Though it's sticky, you smell good now.;You gain +1 clothing and gain +20 pride"
                                                runquote = runtext.split(';')
                                                for x in runquote:
                                                    runquotePoint = Point(500,500)
                                                    runquoteHome = Text(runquotePoint, x)
                                                    runquoteHome.draw(win)
                                                    win.getMouse()
                                                    runquoteHome.undraw()
                                            runningtext()
                             
                                            #youLose()
                                            #win.getMouse()
                                            clothesupdate3 = float(newerclothes + 1)
                                            clothesupdate4 = clothes.setText(clothesupdate3)
                                            #clothesupdateraw3.draw(win)
                                            bulliedtodeath3 = float(bulliedtodeath2 +20 )
                                            bulliedhealth3 = health.setText(bulliedtodeath3)
                                            #bulliedhealth2.draw(win)
                                            
                                            
                                            movingonbabypoint = Point(500,500)
                                            movingonbaby = Text(movingonbabypoint, "You continue forward...")
                                            movingonbaby.draw(win)
                                            win.getMouse()
                                            thedoor()
                                            movingonbaby.setText("They're right there. The pants.")
                                            win.getMouse()
                                            movingonbaby.setText("But just as you're about to open, the door...")
                                            win.getMouse()
                                            movingonbaby.setText("the lights go out.")
                                            win.getMouse()
                                            
                                                                                ##########
                                                                                #ENEMY 3
                                            
                                            def subconsciousenemy3():
        #PICTURE OF THE EYES OPENING.
                                            
                                            #subconscioustextenemy3 = (" blah .")
                                            #exquotessub = subconscioustextenemy3.split(';')
                                            #for x in exquotessub:
                                           #     quotePoint1 = Point(500,400)
                                           #     quoteHome1 = Text(quotePoint1, x)
                                           #     quoteHome1.setStyle("bold italic")
                                           #     quoteHome1.draw(win)
                                           #     win.getMouse()
                                           #     quoteHome1.undraw()
                                            
                                                def convo():
                                                    blackback()
                                                    
                                                    
                                                    #leave on eyes open
                                                    
                                                    
                                                    
                                                    subtopleftback = Point(200,375)
                                                    subbottomrightback = Point(800,420)
                                                    subbackground = Rectangle(subtopleftback, subbottomrightback)
                                                    subbackground.setFill("grey")
                                                    subbackground.draw(win)
                                                    
                                                    selftopleftback = Point(200,475)
                                                    selfbottomrightback = Point(800,520)
                                                    selfbackground = Rectangle(selftopleftback, selfbottomrightback)
                                                    selfbackground.setFill("white")
                                                    selfbackground.draw(win)
                                                    
                                                    
                                                    #set up textbox and text for self
                                                    subconsciousconvoPoint = Point(500,400)
                                                    subconsciousconvo = Text(subconsciousconvoPoint,"hello")
                                                    subconsciousconvo.setStyle("bold italic")
                                                    subconsciousconvo.draw(win)
                                                    win.getMouse()
                                                    subconsciousconvo.undraw()
                                                    
                                                    #set up textbok and text for subconscious
                                                    selfconvoPoint = Point(500,500)
                                                    selfconvo = Text(selfconvoPoint,"hello? who are you?")
                                                    selfconvo.setStyle("bold italic")
                                                    #selfconvobox = rectangle
                                                    selfconvo.draw(win)
                                                    win.getMouse()
                                                    selfconvo.undraw()
                                                    
                                                    subconsciousconvo.setText("i am you")
                                                    subconsciousconvo.draw(win)
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("but i'm me")
                                                    selfconvo.draw(win)
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("true... \ni'm the you that you don't want to see. both your dreams and your nightmares. \nyou're afraid of your truths, you know.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("that's confusing. i just need pants so i can get to my meeting on time.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("the pants are all you see.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("they're glowing yellow in this black and white dream. \nyes, they're all i can see.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("what do you think the pants could represent?")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("i dunno... you tell me.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("that's not my job. i'm just here to call attention to them.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("this is dumb. let me wake up.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("i don't know. i think there's more about yourself you should pay attention to.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("can i get the pants first?")
                                                    win.getMouse()
                                                    
                                                    
                                                    
                                                    
                            #eyes blink.
                                                    
                                                    
                                                    
                                                    subconsciousconvo.setText("will you pay attention to your dreams more?")
                                                    win.getMouse()
                                                    
                                                    
                                                    
                                                    
                                                    listening = Button(win, Point(150, 500), 100, 75,'Promise to\nListen')
                                                    listening.rect.setFill("white")
                                                    listening.activate()

                                                    ignoring = Button(win, Point(850, 500), 100, 75,'Ignore')
                                                    ignoring.rect.setFill("white")
                                                    ignoring.activate()
                                                    
                                                    clickerpoints = win.getMouse()   
                                            
                                                    text.setText("What do you do?")
                                                    
                                                    while True:
                                                        if listening.clicked(clickerpoints):
                                #eyes blink closed.
                                                            listening.deactivate()
                                                            ignoring.deactivate()
                                                            blackback()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            subbackground.draw(win)
                                                            #selfbackground.draw(win)
                                                            subconsciousconvo.draw(win)
                                                            #selfconvo.draw(win)
                                                            
                                                            clothesupdate4 = float(5 + 1)
                                                            clothesupdate4 = str(clothesupdate4)
                                                            bulliedtodeath4 = float(bulliedtodeath2 + 50)
                                                            bulliedtodeath4 = str(bulliedtodeath4)
                                                            
                                                            subconsciousconvo.setText("thank you. here are your pants...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("before you wake up, know you also gained 30 pride.\nyour final scores were...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("Clothes: " + clothesupdate4 + "Pride:" + bulliedtodeath4)
                                                            win.getMouse()
                                                            startandendwindow()
                                                            #you  wake up, feleing well rrested, and sstart searching for another job,
                                                            #or at least a hobby.
                                                            yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                            yourName.draw(win)
                                                            win.getMouse()
                                                            yourName.undraw()
                                                            def endwords():
                                                                runtext = ("You conduct a fantastic meeting.;However, once you're done, you start looking for a new job.;Maybe things will start to make sense.")
                                                                runquote = runtext.split(';')
                                                                for x in runquote:
                                                                    runquotePoint = Point(500,300)
                                                                    runquoteHome = Text(runquotePoint, x)
                                                                    runquoteHome.draw(win)
                                                                    win.getMouse()
                                                                    runquoteHome.undraw()
                                                            endwords()
                                                            #inputBox.undraw()
                                                            #yourName.undraw()
                                                            blackback()
                                                            win.close()
                                                        
                                                        elif ignoring.clicked(clickerpoints):
                                                            
                                                            blackback()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            subbackground.draw(win)
                                                            #selfbackground.draw(win)
                                                            subconsciousconvo.draw(win)
                                                            #selfconvo.draw(win)
                                                            
                                                            clothesupdate4 = float(5)
                                                            clothesupdate4 = str(clothesupdate4)
                                                            bulliedtodeath4 = float(bulliedtodeath2)
                                                            bulliedtodeath4 = str(bulliedtodeath4)
                                                            
                                                            listening.deactivate()
                                                            ignoring.deactivate()
                                                            
                                            
                                                            subconsciousconvo.setText("im sorry. i hope you learn to listen better")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("before you wake up, your final scores were...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("Clothes: " + clothesupdate4 + ", Pride: " + bulliedtodeath4)
                                                            #i'm sorry. hopefully with time you learn to listen better.
        
                                                            win.getMouse()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            #
                                                            startandendwindow()
                                                            

                                                            
                                                            yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                            yourName.draw(win)
                                                            win.getMouse()
                                                            yourName.undraw()
                                                            
                                                            def endwords():
                                                                runtext = "Guess you gotta get back to work;hopefully you don't fall asleep;Also, just one more thing...;You're not wearing pants."
                                                                runquote = runtext.split(';')
                                                                for x in runquote:
                                                                    runquotePoint = Point(500,300)
                                                                    runquoteHome = Text(runquotePoint, x)
                                                                    runquoteHome.draw(win)
                                                                    win.getMouse()
                                                                    runquoteHome.undraw()
                                                            endwords()
                                                            
                                                            blackback()
                                                            win.close()
                                                            #you wake up, disoriented, getting ready for the meeting you hate.
                                                            #what a weird dream.
                                                            #end game.
                                                            
                                                convo()
                                            
                                            subconsciousenemy3()
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                            
    ###_________________________________________________________________________________________________________________________________________________________________________________________________
                                        
                                        elif eatbutton.clicked(clickerpoint):
                                            
                                            stabbutton.deactivate()
                                            eatbutton.deactivate()
                                            completeplayerwindow()
                                            clothes.undraw()
                                            health.undraw()
                                            #playerwindow()
                                            healthandtrinketswindows()
                                            justclotheswindow()
                                            clothes.draw(win)
                                            health.draw(win)
                                            newerclothes = float(initialclothes + 4)
                                            newerclothesdraw = clothes.setText(newerclothes)
                                            #win.getMouse()
                                            bulliedtodeath2 = float(30 + 20)
                                            #health.draw(win)
                                            bulliedhealth1 = health.setText(bulliedtodeath2)
                                            
                                            #bulliedhealth1.draw(win)
                                            
                                            def eatruntext():
                                                runtext = ("You grab the offered a cup of icecreram;It's delicious, but you also quickly learn, as you bite on it, there's a t-shirt inside;The fridge starts laughing at you at his prank.\nThe fact you fell for something so stupid makes you lose -10 pride.;Still, you got a shirt out of it, so you put it on and move on\nwaving to the laughing fridge on the way out.")
                                                runquote = runtext.split(';')
                                                for x in runquote:
                                                    runquotePoint = Point(500,500)
                                                    runquoteHome = Text(runquotePoint, x)
                                                    runquoteHome.draw(win)
                                                    win.getMouse()
                                                    runquoteHome.undraw()
                                                #win.getMouse()
                                                
                                                
                                                
                                            eatruntext()
                             
                                            #youLose()
                                            clothesupdate3 = float(newerclothes + 1)
                                            clothesupdate4 = clothes.setText(clothesupdate3)
                                            #clothesupdateraw3.draw(win)
                                            bulliedtodeath3 = float(bulliedtodeath2 -10 )
                                            bulliedhealth3 = health.setText(bulliedtodeath3)
                                            
                                            win.getMouse()
                                            movingonbabypoint = Point(500,500)
                                            movingonbaby = Text(movingonbabypoint, "You continue forward...")
                                            movingonbaby.draw(win)
                                            win.getMouse()
                                            thedoor()
                                            movingonbaby.setText("They're right there. The pants.")
                                            win.getMouse()
                                            movingonbaby.setText("But just as you're about to open, the door...")
                                            win.getMouse()
                                            movingonbaby.setText("the lights go out.")
                                            win.getMouse()
                                                 
                                            
                                            
                                                                ###### ENEMY THRREE BABY (COPY IT OVERR!!
                                            
                                            
                                                                       
                                            def subconsciousenemy3():
        #PICTURE OF THE EYES OPENING.
                                            
                                            #subconscioustextenemy3 = (" blah .")
                                            #exquotessub = subconscioustextenemy3.split(';')
                                            #for x in exquotessub:
                                           #     quotePoint1 = Point(500,400)
                                           #     quoteHome1 = Text(quotePoint1, x)
                                           #     quoteHome1.setStyle("bold italic")
                                           #     quoteHome1.draw(win)
                                           #     win.getMouse()
                                           #     quoteHome1.undraw()
                                            
                                                def convo():
                                                    blackback()
                                                    
                                                    
                                                    #leave on eyes open
                                                    
                                                    
                                                    
                                                    subtopleftback = Point(200,375)
                                                    subbottomrightback = Point(800,420)
                                                    subbackground = Rectangle(subtopleftback, subbottomrightback)
                                                    subbackground.setFill("grey")
                                                    subbackground.draw(win)
                                                    
                                                    selftopleftback = Point(200,475)
                                                    selfbottomrightback = Point(800,520)
                                                    selfbackground = Rectangle(selftopleftback, selfbottomrightback)
                                                    selfbackground.setFill("white")
                                                    selfbackground.draw(win)
                                                    
                                                    
                                                    #set up textbox and text for self
                                                    subconsciousconvoPoint = Point(500,400)
                                                    subconsciousconvo = Text(subconsciousconvoPoint,"hello")
                                                    subconsciousconvo.setStyle("bold italic")
                                                    subconsciousconvo.draw(win)
                                                    win.getMouse()
                                                    subconsciousconvo.undraw()
                                                    
                                                    #set up textbok and text for subconscious
                                                    selfconvoPoint = Point(500,500)
                                                    selfconvo = Text(selfconvoPoint,"hello? who are you?")
                                                    selfconvo.setStyle("bold italic")
                                                    #selfconvobox = rectangle
                                                    selfconvo.draw(win)
                                                    win.getMouse()
                                                    selfconvo.undraw()
                                                    
                                                    subconsciousconvo.setText("i am you")
                                                    subconsciousconvo.draw(win)
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("but i'm me")
                                                    selfconvo.draw(win)
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("true... \ni'm the you that you don't want to see. both your dreams and your nightmares. \nyou're afraid of your truths, you know.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("that's confusing. i just need pants so i can get to my meeting on time.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("the pants are all you see.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("they're glowing yellow in this black and white dream. \nyes, they're all i can see.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("what do you think the pants could represent?")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("i dunno... you tell me.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("that's not my job. i'm just here to call attention to them.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("this is dumb. let me wake up.")
                                                    win.getMouse()
                                                    
                                                    subconsciousconvo.setText("i don't know. i think there's more about yourself you should pay attention to.")
                                                    win.getMouse()
                                                    
                                                    selfconvo.setText("can i get the pants first?")
                                                    win.getMouse()
                                                    
                                                    
                                                    
                                                    
                            #eyes blink.
                                                    
                                                    
                                                    
                                                    subconsciousconvo.setText("will you pay attention to your dreams more?")
                                                    win.getMouse()
                                                    
                                                    
                                                    
                                                    
                                                    listening = Button(win, Point(150, 500), 100, 75,'Promise to\nListen')
                                                    listening.rect.setFill("white")
                                                    listening.activate()

                                                    ignoring = Button(win, Point(850, 500), 100, 75,'Ignore')
                                                    ignoring.rect.setFill("white")
                                                    ignoring.activate()
                                                    
                                                    clickerpoints = win.getMouse()   
                                            
                                                    text.setText("What do you do?")
                                                    
                                                    while True:
                                                        if listening.clicked(clickerpoints):
                                #eyes blink closed.
                                                            listening.deactivate()
                                                            ignoring.deactivate()
                                                            blackback()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            subbackground.draw(win)
                                                            #selfbackground.draw(win)
                                                            subconsciousconvo.draw(win)
                                                            #selfconvo.draw(win)
                                                            
                                                            clothesupdate4 = float(5 + 1)
                                                            clothesupdate4 = str(clothesupdate4)
                                                            bulliedtodeath4 = float(bulliedtodeath2 + 50)
                                                            bulliedtodeath4 = str(bulliedtodeath4)
                                                            
                                                            subconsciousconvo.setText("thank you. here are your pants...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("before you wake up, know you also gained 30 pride.\nyour final scores were...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("Clothes: " + clothesupdate4 + "Pride:" + bulliedtodeath4)
                                                            win.getMouse()
                                                            startandendwindow()
                                                            #you  wake up, feleing well rrested, and sstart searching for another job,
                                                            #or at least a hobby.
                                                            yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                            yourName.draw(win)
                                                            win.getMouse()
                                                            yourName.undraw()
                                                            def endwords():
                                                                runtext = ("You conduct a fantastic meeting.;However, once you're done, you start looking for a new job.;Maybe things will start to make sense.")
                                                                runquote = runtext.split(';')
                                                                for x in runquote:
                                                                    runquotePoint = Point(500,300)
                                                                    runquoteHome = Text(runquotePoint, x)
                                                                    runquoteHome.draw(win)
                                                                    win.getMouse()
                                                                    runquoteHome.undraw()
                                                            endwords()
                                                            #inputBox.undraw()
                                                            #yourName.undraw()
                                                            blackback()
                                                            win.close()
                                                        
                                                        elif ignoring.clicked(clickerpoints):
                                                            
                                                            blackback()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            subbackground.draw(win)
                                                            #selfbackground.draw(win)
                                                            subconsciousconvo.draw(win)
                                                            #selfconvo.draw(win)
                                                            
                                                            clothesupdate4 = float(5)
                                                            clothesupdate4 = str(clothesupdate4)
                                                            bulliedtodeath4 = float(bulliedtodeath2)
                                                            bulliedtodeath4 = str(bulliedtodeath4)
                                                            
                                                            listening.deactivate()
                                                            ignoring.deactivate()
                                                            
                                            
                                                            subconsciousconvo.setText("im sorry. i hope you learn to listen better")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("before you wake up, your final scores were...")
                                                            win.getMouse()
                                                            subconsciousconvo.setText("Clothes: " + clothesupdate4 + ", Pride: " + bulliedtodeath4)
                                                            #i'm sorry. hopefully with time you learn to listen better.
        
                                                            win.getMouse()
                                                            subbackground.undraw()
                                                            selfbackground.undraw()
                                                            subconsciousconvo.undraw()
                                                            selfconvo.undraw()
                                                            #
                                                            startandendwindow()
                                                            

                                                            
                                                            yourName.setText("'Oh, " + name + ", that was a weird dream,'\nyou say to yourself.")
                                                            yourName.draw(win)
                                                            win.getMouse()
                                                            yourName.undraw()
                                                            
                                                            def endwords():
                                                                runtext = "Guess you gotta get back to work;hopefully you don't fall asleep;Also, just one more thing...;You're not wearing pants."
                                                                runquote = runtext.split(';')
                                                                for x in runquote:
                                                                    runquotePoint = Point(500,300)
                                                                    runquoteHome = Text(runquotePoint, x)
                                                                    runquoteHome.draw(win)
                                                                    win.getMouse()
                                                                    runquoteHome.undraw()
                                                            endwords()
                                                            
                                                            blackback()
                                                            win.close()
                                                            #you wake up, disoriented, getting ready for the meeting you hate.
                                                            #what a weird dream.
                                                            #end game.
                                                            
                                                convo()
                                            
                                            subconsciousenemy3()
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                        else:
                                            
                                            frnewtext = ("Make a choice.")
                                            frnewtexts = Text(Point(500,500), frnewtext)
                                            frnewtexts.draw(win)
                                            win.getMouse()
                                            frnewtexts.setText(" ")
                                            fridgedecisions()
                                fridgedecisions()
                                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
                                    
                            morethan9()       
                      
                            
                            
                        else:
                            stepstext.setText("Please enter a whole number between 1 and 10. \n\nInstructions for dummies: \n\nEnter any of the following: \n1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
                            usersteps = inputBox.getText()
                            win.getMouse()
                            stepsforward()
                        
                stepsforward()
                    
                #else:
                 #       stepstext.setText("Please enter a whole number between 1 and 10. \n\nInstructions for dummies: \n\nEnter any of the following: \n1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
                   #     usersteps = inputBox.getText()
                  #      win.getMouse()
                    #    stepsforward()
                        
                #stepsforward()
                    
                    


                                                    #ENEMY 3
       
    #enemy trinket
    #use random (10,20)
       
                
                
                
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
                
            elif no.clicked(cPoint):
                yes.deactivate()
                no.deactivate()
                blackback()
                win.getMouse()
                win.getMouse()
                win.getMouse()
                playerwindow()
                def youloser():
                    startingquotes = "You wake up from your dream and never got to experience your adventure.;Try again?\n(y/n)"
                    exquotes = startingquotes.split(';')
                    for x in exquotes:
                        quotePoint = Point(500,500)
                        quoteHome = Text(quotePoint, x)
                        quoteHome.draw(win)
                        win.getMouse()
                        quoteHome.undraw()
                def tryorgive():
                    tryagain = Button(win, Point(150, 500), 100, 75,'Try Again')
                    tryagain.rect.setFill("light green")
                    tryagain.activate()

                    # TO ACTIVATE BUTTON: yes.activate()

                    giveup = Button(win, Point(850,500),100,75,"Give Up")
                    giveup.rect.setFill("pink")
                    giveup.activate()
                    
                    newtextpoint = Point(500,500)
                    newtext = Text(newtextpoint, "  ")
                    newtext.draw(win)
                    
                    mouse = win.getMouse()
                    
                    while True:
                        if tryagain.clicked(mouse):
                            #newtext.setText("Try Again")
                            #win.getMouse()
                            newtext.setText(" ")
                            buttons()
                        elif giveup.clicked(mouse):
                            newtext.setText("Something within you is missing. But c'est la vie. Have fun at work.")
                            win.getMouse()
                            win.close()
                        else:
                            newtext.setText("Choose Yes or No")
                            win.getMouse()
                            newtext.setText(" ")
                            tryorgive()
                            
                youloser()
                tryorgive()
     
            else:
                text.setText("Choose Yes or No")
                win.getMouse()
                text.setText(" ")
                buttons()
    #    if yes.clicked(cPoint) or no.clicked(cPoint):
    #        yes.deactivate() and no.deactivate() and yes.close()
        #if there's a ? then post the options for a yes.
                #if yes, then continue loop. if no, you lose
        
    #PLAYER SPEECH BUBBLE

            
        
    buttons()



                #if mouse is pressed, move forward.



















       
main()
   
                                                #END GAME



#block stating total trinkets

#block stating total health

            #if user has any health AND 5 trinkets (clothes), you win. you wake up feeling refreshed, ready to give a trainin 
            #else you lose :( you wake up unprepared for your work meetin 

#close window
win.getMouse()
win.close()
