def run(): # Entire program runs in one singular function.
    from graphics import Circle, Point, GraphWin, color_rgb, Text, Entry, Rectangle
    from math import sin, cos, radians, sqrt
    from time import sleep
    from random import randint



    km_to_au = 1/1.496e+8  # Calculation of km to astronomical units for the orbit calculations.


    class Planet:                           # creates Planet objects
        def __init__(self, x, y, color, radius, distance):
            self.x = x
            self.y = y
            self.color = color
            self.radius = radius
            self.distance = distance
            self.Circle = Circle(Point(self.x, self.y), self.radius)
            self.Circle.setFill(self.color)

        def draw(self, window):
            self.Circle.draw(window)


    class Orbit:                                # Draws the white circles that the planets orbit on
        def __init__(self, x, y, oradius):
            self.x = x
            self.y = y
            self.oradius = oradius
            self.Circle = Circle(Point(self.x, self.y), self.oradius)
            self.Circle.setOutline("white")

        def draw(self, window):
            self.Circle.draw(window)


    def quit():                      # Function to display a "closing window" message and close the window after 1.1 seconds
        textbox.undraw()
        menu.undraw()
        sleep(0.1)
        closemessage = Text(Point(375, 40), "closing window...")
        closemessage.setSize(20)
        closemessage.setFace("times roman")
        closemessage.setTextColor(color_rgb(155, 155, 155))
        closemessage.setStyle("italic")
        closemessage.draw(window)
        sleep(1)
        
    windowlength = 750                                         # Sets window properties within variables for use later.
    windowheight = 750
    window = GraphWin("Solar System", windowlength, windowheight)
    window.setBackground("white")


    start_label = Text(Point(375, 375), "Click anywhere to start.")  # The following code creates the "start" window
    start_label.setSize(30)                                          # when you first run the code.
    start_label.setFill(color_rgb(155, 155, 155))
    start_label.setStyle("italic")
    start_label.setStyle("bold")
    start_label.draw(window)
    start_loc = window.getMouse()


    if start_loc == False:                  # Waits for mouse click to undraw the text on the
        pass                                # start screen and set background to black.
    else:
        start_label.undraw()

    window.setBackground("black")

    sun_radius=(6963400000)*km_to_au                               # The following code creates the planets as objects
    sun = Planet(375, 375, color_rgb(253, 184, 19), sun_radius, 0) # of the project class and draws them on the window,
    sun.draw(window)                                               # while calculating the proper radius according to
                                                                   # the km to au calculation.


    mercury_distance = 57.91e6 * km_to_au*0.75
    mercury_radius=(2439700000)*km_to_au


    mercury = Planet(375 + mercury_distance*375*0.75, 375, color_rgb(219, 206, 202), mercury_radius, mercury_distance)
    mercury_orbit = Orbit(375, 375, mercury_distance*375*0.75)
    mercury.draw(window)
    mercury_orbit.draw(window)


    venus_radius=(6051800000)*km_to_au*0.75
    venus_distance = 108.2e6 * km_to_au

    venus = Planet(375 + venus_distance*375*0.75, 375, color_rgb(255, 198, 73), venus_radius, venus_distance)
    venus_orbit = Orbit(375, 375, venus_distance*375*0.75)
    venus.draw(window)
    venus_orbit.draw(window)


    earth_radius=(6378140000)*km_to_au*0.75
    earth_distance = 149.6e6 * km_to_au


    earth = Planet(375 - earth_distance*375*0.75, 375, color_rgb(52, 165, 111), earth_radius, earth_distance)
    earth_orbit = Orbit(375, 375, earth_distance*375*0.75)
    earth.draw(window)
    earth_orbit.draw(window)


    for i in range(500):                    # This for loop draws 500 "stars"
        x = randint(0, 750)                # at random points within the window.
        y = randint(0, 750)
        message = Text(Point(x, y), "*")
        message.setSize(5)
        message.setTextColor("white")
        message.draw(window)

    cometstart = Rectangle(Point(650, 650), Point(800, 800))  # "cometstart" is the box that the
    cometstart.setOutline("white")                            # comet "lives" in before it is moved.
    cometstart.draw(window)

    cometinitialX = 700
    cometinitialY = 700                     # The following code defines the
    cometRadius = 18                        # properties of the comet.

    comet = Circle(Point(cometinitialX, cometinitialY), cometRadius)
    comet.setFill("grey")
    comet.draw(window)

    cometHome = Text(Point(690, 610), """
    Comets live 
    in boxes.""")                                # "cometHome" is the text above "cometstart".
    cometHome.setSize(12)
    cometHome.setTextColor("white")
    cometHome.draw(window)

    alreadycheckedMercury = False  # These checks are set so if Mercury has already intersected 
    alreadycheckedVenus = False    # with the comet and been undrawn, the program will not attempt
    alreadycheckedEarth = False    # to undraw Mercury over and over again.

    cometflown = False      # This check is set so if the comet has already been flown (and therefore been undrawn),   
                            # the program will not attempt to continue "flying" the comet.



    menu = Text(Point(375, 10), """Type "q" to quit the simulation.""")
    menu.setFill(color_rgb(155, 155, 155))
    menu.setSize(12)    # This is the text for the quit instructions at the top middle of the screen.
    menu.draw(window)

    textbox = Entry(Point(375, 35), 4)  # This is the textbox directly below the "menu" (quit instructions).
    textbox.draw(window)


    angle_mercury = 0   # Setting initial angles before the planets begin to orbit.
    angle_venus = 0
    angle_earth = 0


    while not window.isClosed():     # checks that the window is not closed: 
        if not cometflown:           # chekcs if the comet has not flown 
            pt=window.checkMouse()   # gets a point from the mouse click
            if pt!=None:             # checks if there has been a mouse click
                cometUserpts = window.getMouse()  # gets the user points from the window 
                cometUserXpt = cometUserpts.getX()  # Takes this point and gets the x value.
                cometUserYpt = cometUserpts.getY()  # Takes this point and gets the y value.

                # "distanceComet2Pt" calculates the distance from the user's mouse click to the comet.
                distanceComet2Pt = sqrt(((cometinitialX - cometUserXpt) ** 2) + ((cometinitialY - cometUserYpt) ** 2))

                # Calculate x and y vectors, so the comet can be moved by this number.
                # Multiply the x and y vectors by 15 to control the speed at which the comet will move.
                Xvector = ((cometUserXpt - cometinitialX) / distanceComet2Pt) * 15
                Yvector = ((cometUserYpt - cometinitialY) / distanceComet2Pt) * 15
                cometflown=True 

        key = window.checkKey()    # Allows for user input into the textbox.
        key = key.lower()          # Turns this input into lowercase, so it can always be compared properly.

        if key == "q":
            quit()                  # If user inputs "q", the program will use the
            break                   # "quit" function and close the graphics window.

        if cometflown:  # checks if the comet has been flown
            comet.move(Xvector, Yvector)

            # Will continually get the comet's x and y center points to compare to the planet points.
            cometXpoint = (comet.getCenter()).getX()
            cometYpoint = (comet.getCenter()).getY()

            # Calculates the disatnce between the center's of the planets and the comet.
            Mercury_CometDistance = sqrt(((int(cometXpoint - mercury.x))**2) + ((int(cometYpoint - mercury.y))**2)) 
            Venus_CometDistance =sqrt (((int(cometXpoint - venus.x))**2) + ((int(cometYpoint - venus.y))**2))
            Earth_CometDistance = sqrt(((int(cometXpoint - earth.x))**2) + ((int(cometYpoint - earth.y))**2))


                # The following code will continually compare the distance between the comet and the planet to the sum of the planet's
                # radius and the comet's radius. If the distance between the two are less than the sum of the radi,
                # then we know they have intersected. The planet will be undrawn, and two messages will show 0.6 seconds
                # apart.

            if Mercury_CometDistance < (mercury_radius + cometRadius):  # Checks for a collision between Mercury and the comet 
                if alreadycheckedMercury == False:
                    alreadycheckedMercury = True
                    mercury.Circle.undraw()
                    hitMmessage = Text(Point(mercury.x, mercury.y),"KABOOM!!!")
                    hitMmessage.setFill("red")
                    hitMmessage.setSize(30)
                    hitMmessage.draw(window)
                    sleep(0.6)
                    hitMmessage.setSize(15)
                    hitMmessage.setFill("white")
                    hitMmessage.setText("You've hit Mercury!")

            if Venus_CometDistance < (venus_radius + cometRadius):  # Checks for a collision between Venus and the comet 
                if alreadycheckedVenus == False:
                    alreadycheckedVenus = True
                    venus.Circle.undraw()
                    hitVmessage = Text(Point(venus.x, venus.y),"KABOOM!!!")
                    hitVmessage.setFill("red")
                    hitVmessage.setSize(30)
                    hitVmessage.draw(window)
                    sleep(0.6)
                    hitVmessage.setSize(15)
                    hitVmessage.setFill("white")
                    hitVmessage.setText("You've hit Venus!")

            if Earth_CometDistance < (earth_radius + cometRadius):  # Checks for a collision between Earth and the comet 
                if alreadycheckedEarth == False:
                    alreadycheckedEarth = True
                    earth.Circle.undraw()
                    hitEmessage = Text(Point(earth.x, earth.y),"KABOOM!!!")
                    hitEmessage.setFill("red")
                    hitEmessage.setSize(30)
                    hitEmessage.draw(window)
                    sleep(0.6)
                    hitEmessage.setSize(15)
                    hitEmessage.setFill("white")
                    hitEmessage.setText("You've hit Earth!")

            
            # The following code will compare the edges of the comet to the window length and window height.
            # This will let us know when the comet has left the window and will undraw the comet once this has happened.
            cometLeftEdge = comet.getCenter().getX() - cometRadius
            cometRightEdge = comet.getCenter().getX() + cometRadius
            cometTopEdge = comet.getCenter().getY() - cometRadius
            cometBottomEdge = comet.getCenter().getY() + cometRadius

            if (cometLeftEdge <= 0 or cometRightEdge >= windowlength) or (cometTopEdge <= 0 or cometBottomEdge >= windowheight):
                    comet.undraw()
                    cometflown = True

        
        # Orbit the planets. Continously rotates the planets around the sun with their orbits 
        mercury_x = 375 + mercury.distance*375*0.75 * cos(radians(angle_mercury))
        mercury_y = 375 + mercury.distance*375*0.75 * sin(radians(angle_mercury))
        venus_x = 375 + venus.distance*375*0.75 * cos(radians(angle_venus))
        venus_y = 375 + venus.distance*375*0.75 * sin(radians(angle_venus))
        earth_x = 375 - earth.distance*375*0.75 * cos(radians(angle_earth))
        earth_y = 375 - earth.distance*375*0.75 * sin(radians(angle_earth))


        mercury.Circle.move(mercury_x - mercury.x, mercury_y - mercury.y) # moves the planet Mercury 
        mercury.x = mercury_x
        mercury.y = mercury_y


        venus.Circle.move(venus_x - venus.x, venus_y - venus.y) # moves the planet Venus 
        venus.x = venus_x
        venus.y = venus_y


        earth.Circle.move(earth_x - earth.x, earth_y - earth.y) # moves the planet Earth 
        earth.x = earth_x
        earth.y = earth_y


        angle_mercury += 360 / 88  # 88 days
        angle_venus += 360 / 225  # 225 days
        angle_earth += 360 / 365  # 365 days

        sleep(0.01)

run()