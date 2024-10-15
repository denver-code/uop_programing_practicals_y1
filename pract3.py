from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(100, 100), "Hello graphix!")
    message.draw(win)
    win.get_mouse()


def two_points():
    my_win = Window("My Window", 330, 160)
    p = Point(30, 90)
    p.draw(my_win)
    p.move(70, -40)

    q = Point(200, 125)
    q.draw(my_win)

    p.outline_colour = "blue"
    q.outline_colour = "red"


def hello_circles():
    win = Window()
    centre = Point(200, 200)
    circle_1 = Circle(centre, 20)
    circle_1.draw(win)

    circle_2 = Circle(Point(150, 100), 50)
    circle_2.draw(win)

    circle_1.outline_width = 7
    circle_1.outline_colour = "blue"
    circle_2.outline_colour = "red"
    circle_2.fill_colour = "green"
    circle_1.fill_colour = "yellow"

    circle_2.move(100, 150)
    print("circle_2's radius =", circle_2.radius)
    print("circle_2's centre =", circle_2.radius)


def hello_lines():
    win = Window()
    line_1 = Line(Point(50, 150), Point(350, 250))
    line_1.draw(win)

    line_1.move(0, 100)
    line_1.outline_width = 5
    line_1.outline_colour = "red"

    start = Point(0, 200)
    end = Point(200, 0)
    line_2 = Line(start, end)
    line_2.draw(win)

    print("line_1 starts at", line_1.get_p1())
    print("line_1 ends at", line_1.get_p2())


def hello_rectangles():
    win = Window()
    rectangle = Rectangle(Point(50, 190), Point(350, 310))
    rectangle.draw(win)
    rectangle.fill_colour = "black"

    square = Rectangle(Point(150, 50), Point(250, 150))
    square.draw(win)
    square.fill_colour = "white"


def hello_triangle():
    win = Window()
    points = [Point(200, 50), Point(50, 250), Point(350, 250)]
    triangle = Polygon(points)
    triangle.draw(win)
    triangle.fill_colour = "red"
    win.get_mouse()


def hello_hexagon():
    win = Window()
    points = [
        Point(200, 50), Point(150, 100), Point(150, 200),
        Point(200, 250), Point(250, 200), Point(250, 100)
    ]
    hexagon = Polygon(points)
    hexagon.draw(win)
    hexagon.fill_colour = "blue"
    win.get_mouse()

    hello_hexagon()


def hello_text():
    win = Window()
    message = Text(Point(200, 200), "Hello World")
    message.draw(win)
    message.size = 20
    message.typeface = "times roman"
    message.text_colour = "magenta"

    win.get_mouse()
    message.text = "Goodbye"


def hello_entry():
    win = Window("Greeter", 400, 400)
    message = Text(Point(200, 100), "Enter your name & click on the window")
    message.draw(win)

    input_box = Entry(Point(200, 200), 10)
    input_box.draw(win)

    win.get_mouse()
    message.text = "Hello, " + input_box.text


def click_test():
    win = Window("Keep on clicking me!")
    for i in range(10):
        p = win.get_mouse()
        x = p.x
        y = p.y
        location = Text(p, str(x) + " " + str(y))
        location.draw(win)


def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)

    left_arm = Line(Point(200, 200), Point(260,170))
    left_arm.draw(win)

    right_arm = Line(Point(200, 200), Point(140,170))
    right_arm.draw(win)

    left_leg = Line(Point(200, 240), Point(175,290))
    left_leg.draw(win)


    right_leg = Line(Point(200, 240), Point(225,290))
    right_leg.draw(win)

    win.get_mouse()


def draw_circle():
    circle_radius = int(input("Please enter radius of the circle:"))
    
    win = Window()
    centre = Point(200, 200)

    circle = Circle(centre, circle_radius)
    circle.draw(win)

    win.get_mouse()


def draw_archery_target():
    win = Window("Archery Target")
    centre = Point(200, 200)
    
    blue_circle =  Circle(centre, 150)
    blue_circle.fill_colour = "blue"
    blue_circle.draw(win)

    red_circle =  Circle(centre, 100)
    red_circle.fill_colour = "red"
    red_circle.draw(win)

    yellow_circle =  Circle(centre, 50)
    yellow_circle.fill_colour = "yellow"
    yellow_circle.draw(win)

    win.get_mouse()


def draw_rectangle():
    rectangle_width = int(input("Please enter rectangle width:"))
    rectangle_height = int(input("Please enter rectangle height:"))

    win = Window()


    horizontal_padding = (400 - rectangle_width)//2
    vertical_padding = (400 - rectangle_height)//2

    rectangle = Rectangle(
        Point(
            horizontal_padding, vertical_padding),
        Point(
            rectangle_width + horizontal_padding, rectangle_height+vertical_padding)
    )

    rectangle.draw(win)
    rectangle.fill_colour = "black"

    win.get_mouse()


def blue_circle():
    win = Window()

    p = win.get_mouse()
    x = p.x
    y = p.y

    circle = Circle(Point(x,y), 100)
    circle.fill_colour = "blue"
    circle.draw(win)

    win.get_mouse()


def draw_line():
    win = Window()

    p1 = win.get_mouse()
    x1 = p1.x
    y1 = p1.y

    p2 = win.get_mouse()
    x2 = p2.x
    y2 = p2.y

    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)

    win.get_mouse()

def ten_lines():
    win = Window()

    for _ in range(10):
        p1 = win.get_mouse()
        x1 = p1.x
        y1 = p1.y

        p2 = win.get_mouse()
        x2 = p2.x
        y2 = p2.y

        line = Line(Point(x1, y1), Point(x2, y2))
        line.draw(win)

    win.get_mouse()


def ten_strings():
    win = Window("Ten Strings", 400, 400)

    input_box = Entry(Point(200, 15), 10)
    input_box.draw(win)

    for _ in range(10):
        p = win.get_mouse()
        message = Text(Point(p.x, p.y), input_box.text)
        message.draw(win)

    win.get_mouse()


def ten_coloured_rectangles():
    """
    Write a ten_coloured_rectangles function to allow the user to draw 10 coloured rectangles
    on the screen. The user should pick the coordinates of the top-left and bottom-right corners
    of every rectangle by clicking on the window.
    """
    pass
