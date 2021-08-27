from maze import obstacles


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
    if "silent_mode" not in robot.keys():
        if movement == "turned":
            print(f" > {robot['name']} turned {steps}.")
        else:
            print(f" > {robot['name']} moved {movement} by {steps} steps.")


def display_robot_position(robot):
    """
    Displays robots current position.

    Args:
        robot: A dictionary that represents the robots attributes.

    Returns:
        N/A
    """

    if "silent_mode" not in robot.keys():
        print(f" > {robot['name']} now at position ({robot['position_x']},{robot['position_y']}).")


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


def display_obstacles():
    """
    Displays all the obstacles in the robot world.

    Args:
        N/A

    Returns:
        N/A
    """

    obstacles_list = obstacles.get_obstacles()
    if len(obstacles_list) > 0:
        print("There are some obstacles:")
        for obstacle in obstacles_list:
            print(f"- At position {obstacle[0]},{obstacle[1]} (to {obstacle[0]+4},{obstacle[1]+4})")


def on_boundary(robot, border):
    """
    Checks if a robot is on the boundary or at least one move away.

    Args:
        robot: A dictionary representing a robot state.
        border: A string indicating which side of the maze the robot should go.

    Returns:
        _: A bool indicating if a robot is on the boundary.
    """

    if border == "top" and robot["position_y"] == 300:
        return True
    if border == "bottom" and robot["position_y"] == -300:
        return True
    if border == "left" and robot["position_x"] == -300:
        return True
    if border == "right" and robot["position_x"] == 300:
        return True
    return False
