import random


def create_obstacles():
    """
    Randomly creates a random number of coordinates that act as obstacles.

    Args:
        N/A

    Returns:
        obstacles: A list of tuples representing obstacles in the robot world.
    """

    obstacles = []
    number_of_obstacles = random.randint(1, 10)
    for _ in range(1, number_of_obstacles + 1):
        obstacle = (random.randint(-300, 300), random.randint(-300, 300))
        obstacles.append(obstacle)
    return obstacles


def create_obstacle_list(obstacle):
    """
    Creates a list of all the coordinates in an L shaped obstacle.

    Args:
        obstacle: A tuple representing the coordinate of the obstacle.

    Returns:
        _: A list of coordinates of the L shaped obstacle.
    """

    obstacle_list_x = [(obstacle[0], obstacle[1] + i) for i in range(0,20)]
    obstacle_list_y = [(obstacle[0] + i, obstacle[1] + 19) for i in range(1,8)]
    return obstacle_list_x + obstacle_list_y


def in_obstacle_list(coordinate,obstacle):
    """
    Checks if the coordinate is in the obstacles list.

    Args:
        coordinate: A tuple representing the x,y coordinate.
        obstacle: A tuple representing the x,y coordinates of the obstacle.

    Returns:
        _: A bool indicating if coordinate is in the obstacle list.
    """

    for item in create_obstacle_list(obstacle):
        if item[0] == coordinate[0] and item[1] == coordinate[1]:
            return True
    return False



def is_position_blocked(x, y):
    """
    Checks if a position is within an obstacle.

    Args:
        x: An integer representing the x coordinate.
        y: An integer representing the y coordinate.

    Returns:
        _: A bool indicating if a position is blocked or not.
    """

    for obstacle in global_obstacles:
        if in_obstacle_list((x,y), obstacle):
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


def get_obstacles():
    """
    Retrieves a list of obstacles.

    Arguments:
        N/A

    Returns:
        _: A list of obstacle objects.
    """

    return global_obstacles


global_obstacles = create_obstacles()
