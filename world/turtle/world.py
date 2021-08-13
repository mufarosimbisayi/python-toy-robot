import turtle as turtle_module
from ..maze import mufaros_maze as obstacles

screen = turtle_module.getscreen()
turtle = turtle_module.Turtle()
boundary = turtle_module.Turtle()


def display_robot_position(robot):
    return


def display_robot_movement(robot, command):
    """
    Displays the robots movement onto the terminal.

    Args:
        robot_name: A string representing the name of the robot.
        command: A string representing the movement command given to the robot.

    Returns:
        N/A
    """

    movement = command.split()[0].strip()
    steps = command.split()[1].strip()
    if movement == "turned":
        movement = f"turtle.{steps}(90)"
        eval(movement)
    else:
        movement = f"turtle.{movement}({steps})"
        eval(movement)


def draw_new_obstacle(obstacle):
    """
    Displays robots current position.

    Args:
        robot: A dictionary that represents the robots attributes.

    Returns:
        N/A
    """

    obstacle_list = obstacles.create_obstacle_list(obstacle)
    turtle.penup()
    for coordinate in obstacle_list:
        turtle.goto(int(coordinate[0]), int(coordinate[1]))
        turtle.pendown()
        turtle.speed(10)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()


def within_limit(robot):
    """
    Checks if the robots movements are within limit.

    Args:
        robot: A dictionary that represents the robots attributes.
        command: A string representing the forward or backward movement and steps.

    Returns:
        _: A boolean value indicating true if the robot is within limits.
    """

    x_range = range(-300,301)
    y_range = range(-300,301)
    if robot["position_x"] in x_range and robot["position_y"] in y_range:
        return True
    return False


def move_robot_starting_position(x,y):
    """
    Moves the starting point of the turtle cursor to position x,y

    Args:
        x: An integer representing the x coordinate.
        y: An integer representing the y coordinate.

    Returns:
        N/A
    """

    boundary.penup()
    boundary.goto(x,y)
    boundary.pendown()


def draw_robot_limit():
    """
    Draws the boundary within which the robot can operate.

    Args:
        N/A

    Returns:
        N/A
    """

    boundary.pencolor("green")
    boundary.pensize(10)
    boundary.speed(10)
    move_robot_starting_position(-300, -300)
    for _ in range(3):
        boundary.forward(600)
        boundary.left(90)
    boundary.forward(600)


def draw_obstacle(x_start, y_start):
    """
    Draws an obstacle within the robot world.

    Args:
        N/A

    Returns:
        N/A
    """

    boundary.pencolor("green")
    boundary.pensize(2)
    boundary.speed(10)
    move_robot_starting_position(x_start, y_start)
    for _ in range(3):
        boundary.forward(4)
        boundary.left(90)
    boundary.forward(4)


def draw_obstacles():
    """
    Draws the obstacles within the robot world.

    Args:
        N/A

    Returns:
        N/A
    """

    for obstacle in obstacles.get_obstacles():
        draw_new_obstacle(obstacle)


def display_robot_replay(robot, commands_replayed):
    """
    Displays the number and circumstance of the replayed commands.

    Args:
        robot: A dictionary that represents the robots attributes.
        commands_replayed: An integer representing commands replayed.

    Returns:
        N/A
    """

    extra = ""
    if "reverse_mode" in robot.keys():
        extra += " in reverse"
        del robot["reverse_mode"]
    if "silent_mode" in robot.keys():
        extra += " silently"
        del robot["silent_mode"]
    print(f" > {robot['name']} replayed {commands_replayed} commands{extra}.")


draw_robot_limit()
draw_obstacles()
