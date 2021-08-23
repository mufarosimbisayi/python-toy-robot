import random


def create_inner_maze():
    """
    Creates the inner part of a maze.

    Args:
        N/A

    Returns:
        maze_list: A list of tuples representing the maze in the robot world.
    """

    x,y = -80,-100
    maze_list = []
    maze_list += [(x + i, y) for i in range(0,161)]
    x,y = 100,-80
    maze_list += [(x, y + i) for i in range(0,161)]
    x,y = 80,100
    maze_list += [(x - i, y) for i in range(0,161)]
    x,y = -100,80
    maze_list += [(x, y - i) for i in range(0,161)]
    return maze_list


def create_outer_maze():
    """
    Creates the outer obstacles in the maze.

    Args:
        N/A

    Returns:
        maze_list: A list of tuples representing the outer part of the maze.
    """

    maze_list = []
    x,y = -200,-200
    maze_list += [(x + i, y) for i in range(0,181)]
    x,y = 20,-200
    maze_list += [(x + i, y) for i in range(0,181)]
    x,y = 200,-200
    maze_list += [(x, y + i) for i in range(0,181)]
    x,y = 200,20
    maze_list += [(x, y + i) for i in range(0,181)]
    x,y = 200,200
    maze_list += [(x - i, y) for i in range(0,181)]
    x,y = -20,200
    maze_list += [(x - i, y) for i in range(0,181)]
    x,y = -200,200
    maze_list += [(x, y - i) for i in range(0,181)]
    x,y = -200,-20
    maze_list += [(x, y - i) for i in range(0,181)]
    return maze_list


def is_position_blocked(x, y):
    """
    Checks if a position is within an obstacle.

    Args:
        x: An integer representing the x coordinate.
        y: An integer representing the y coordinate.

    Returns:
        _: A bool indicating if a position is blocked or not.
    """

    for obstacle in global_maze:
        if x == obstacle[0] and y == obstacle[1]:
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks if there is an obstacle in the paths between the coordinates.

    Args:
        x1: The x coordinate for the first point.
        y1: The y coordinate for the first point.
        x2: The x coordinate for the second point.
        y2: The y coordinate for the second point.

    Returns:
        _: A bool indicating an obstacle in the path.
    """

    if y1 == y2 and x1 != x2:
        if x2 > x1:
            x_range = range(x1, x2 + 1)
        else:
            x_range = reversed(range(x2, x1 + 1))
        for x in x_range:
            if is_position_blocked(x, y1):
                return True
    elif x1 == x2 and y1 != y2:
        if y2 > y1:
            y_range = range(y1, y2 + 1)
        else:
            y_range = reversed(range(y2, y1 + 1))
        for y in y_range:
            if is_position_blocked(x1, y):
                return True
    elif x1 == x2 and y1 == y2:
        if is_position_blocked(x1,y1):
            return True
    return False


def get_maze():
    """
    Retrieves a list of obstacles.

    Arguments:
        N/A

    Returns:
        _: A list of obstacle objects.
    """

    return global_maze


global_maze = create_inner_maze() + create_outer_maze()
