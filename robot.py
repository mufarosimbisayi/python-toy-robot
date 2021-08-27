import sys
import random
from importlib import import_module
from import_helper import dynamic_world_import
from import_helper import dynamic_import
world = dynamic_world_import(sys.argv)
maze = dynamic_import(sys.argv)

def get_robot_name():
    """
    Gets robot name as input from user.

    Args:
        N/A

    Return:
        _: A string representing the robots name.
    """

    return input("What do you want to name your robot? ")


def robot_response(robot_name, response):
    """
    Writes a robots response to the terminal.

    Args:
        response: A string representing a robots response.
        robot_name: A string representing the name of the robot responding.

    Returns:
        N/A
    """

    print(f"{robot_name}: {response}")


def valid_command_list():
    """
    Returns a list of all valid commands.

    Args:
        N/A

    Returns:
        total_commands: A list of strings representing valid commands.
    """

    movement_commands = ["forward", "back", "left", "right", "sprint", "mazerun"]
    replay_commands = ["replay", "reversed", "silent"]
    system_commands = ["help", "off", "top", "bottom"]
    total_commands = movement_commands + replay_commands + system_commands
    return total_commands


def contains_digit(command):
    """
    Checks if a string contains a digit as a standalone or a range n-m.

    Args:
        command: A string representing a command that might contain a digit.

    Returns:
        _: A true boolean value if the command contains a valid digit.
    """

    if command.isdigit():
        return True
    elif len(command.split("-")) == 2:
        command_range = command.split("-")
        if command_range[0].isdigit() and command_range[1].isdigit():
            return True
    else:
        return False



def valid_command(command):
    """
    Checks if a command is valid.

    Args:
        command: A string representing the command.

    Returns:
        _: A boolean value indicating if the command is valid or not.
    """

    command = command.strip().split()
    command_list = valid_command_list()
    if len(command) == 0:
        return False
    elif len(command) == 1 and command[0].lower() in command_list:
        return True
    elif len(command) == 1 and command[0].lower() not in command_list:
        return False

    command = list(map(lambda x: x.lower(), command))
    filtered_list = list(filter(lambda x: True if x in command_list or contains_digit(x) else False, command))
    if len(command) == len(filtered_list):
        return True
    return False


def get_command(robot_name):
    """
    Gets a command from the user.

    Args:
        robot_name: A string representing the name of the robot.

    Returns:
        command: A string representing a valid command.
    """

    command = input(f"{robot_name}: What must I do next? ")
    while(not valid_command(command)):
        robot_response(robot_name, f"Sorry, I did not understand '{command}'.")
        command = input(f"{robot_name}: What must I do next? ")
    return command.lower()


def display_shut_down(robot_name):
    """
    Exits the program.

    Args:
        N/A

    Returns:
        N/A
    """

    robot_response(robot_name, "Shutting down..")
    return


def display_help():
    """
    Displays the robots capabilities.

    Args:
        N/A

    Returns:
        N/A
    """

    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("REPLAY - redo all the movement commands")


def check_obstacles(robot_one, robot_two):
    """
    Checks if there is an obstacle between the path from r one to r two.

    Args:
        robot_one: The initial state of the robot.
        robot_two: The state of a robot after it has made a move.

    Returns:
        _: A bool indicating the existence of an obstacle.
    """

    if maze and maze.is_path_blocked(robot_one["position_x"],robot_one["position_y"],robot_two["position_x"],robot_two["position_y"]):
        robot_response(robot_two["name"], "Sorry, there is an obstacle in the way.")
        return True
    return False


def check_limit(robot_one):
    """
    Checks if the robots new position is within limit.

    Args:
        robot_one: The new robot state after movement.

    Returns:
        _: A bool that indicates if new robot state is within limit.
    """

    if not world.within_limit(robot_one):
        robot_response(robot_one["name"], "Sorry, I cannot go outside my safe zone.")
        return True
    return False


def move_forward(robot, steps):
    """
    Moves a robot forwards by the number of steps.

    Args:
        robot: A dictionary that represents the robots attributes.
        steps: A digit string representing the number of steps moved.

    Returns:
        N/A
    """

    robot_saved_state = robot.copy()
    if len(steps.split()) > 1:
        steps = steps.split()[1].strip()
    if robot["direction"] == "N":
        robot["position_y"] += int(steps)
    elif robot["direction"] == "S":
        robot["position_y"] -= int(steps)
    elif robot["direction"] == "W":
        robot["position_x"] += int(steps)
    elif robot["direction"] == "E":
        robot["position_x"] -= int(steps)
    if check_limit(robot):
        return robot_saved_state
    if check_obstacles(robot_saved_state, robot):
        return robot_saved_state
    world.display_robot_movement(robot, f"forward {steps}")
    return robot


def move_back(robot, steps):
    """
    Moves a robot backwards by the number of steps.

    Args:
        robot: A dictionary that represents the robots attributes.
        steps: A digit string representing the number of steps moved.

    Returns:
        N/A
    """

    robot_saved_state = robot.copy()
    if len(steps.split()) > 1:
        steps = steps.split()[1].strip()
    if robot["direction"] == "N":
        robot["position_y"] -= int(steps)
    elif robot["direction"] == "S":
        robot["position_y"] += int(steps)
    elif robot["direction"] == "W":
        robot["position_x"] -= int(steps)
    elif robot["direction"] == "E":
        robot["position_x"] += int(steps)
    if check_limit(robot):
        return robot_saved_state
    if check_obstacles(robot_saved_state, robot):
        return robot_saved_state
    elif "silent_mode" not in robot.keys():
        world.display_robot_movement(robot, f"back {steps}")
    return robot


def turn(robot, command):
    """
    Turns the robot left or right.

    Args:
        robot: A dictionary that represents the robots attributes.
        command: A string representing left or right.

    Returns:
        robot: A dictionary that represents the robots attributes.

    """

    if command == "left":
        left_map = {"S":"W", "N":"E", "W":"N", "E":"S"}
        robot["direction"] = left_map[robot["direction"]]
    elif command == "right":
        right_map = {"N":"W", "W":"S", "E":"N", "S":"E"}
        robot["direction"] = right_map[robot["direction"]]
    if "silent_mode" not in robot.keys():
        world.display_robot_movement(robot, f"turned {command}")
    return robot


def sprint(robot, command):
    """
    Adds a factorial of sprint value to the x or y position.

    Args:
        robot: A dictionary that represents the robots attributes.

        command: A string representing a sprint command and sprint value.

    Returns:
        robot:
    """

    steps = int(command.split()[1].strip())
    for i in reversed(range(1, steps + 1)):
        movement = f"forward {i}"
        robot = move_forward(robot, movement)
    return robot


def add_command_to_history(robot, command):
    """
    Add a command to the robots command history.

    Args:
        robot: A dictionary that represents the robots attributes.
        command: A string representing the command to be executed.
       
    Returns:
        robot: A dictionary that represents the robots attributes.
    """

    robot["command_history"].append(command)
    return robot


def retrieve_command_history(robot):
    """
    Retrieve a command list representing all the commands executed thus far.

    Args:
        robot: A dictionary that represents the robots attributes.

    Returns:
        _: A list of all the commands executed thus far.
    """

    return robot["command_history"]


def retrieve_movement_commands(robot):
    """
    Retrieve a command list representing all the movement commands executed thus far.

    Args:
        robot: A dictionary that represents the robots attributes.

    Returns:
        _: A list of all the movement commands executed thus far.
    """

    movement_commands = ["forward", "back", "left", "right", "sprint"]
    command_history = retrieve_command_history(robot)

    return list(filter(lambda x: True if x.split(" ")[0] in movement_commands else False, command_history))


def activate_silent_mode(command):
    """
    Check if the silent mode has been requested.

    Args:
        command: A string representing the command to be executed.

    Returns:
        _: Boolean value indicating whether the silent mode has been requested.
    """

    silent_list = list(filter(lambda x: True if x == "silent" or x == "replay" else False, command.split()))
    if len(silent_list) == 2:
        return True
    return False


def activate_reverse_mode(command):
    """
    Check if the reverse mode has been requested.

    Args:
        command: A string representing the command to be executed.

    Returns:
        _: Boolean value indicating whether the reverse mode has been requested.
    """

    reverse_list = list(filter(lambda x: True if x == "reversed" or x == "replay" else False, command.split()))
    if len(reverse_list) == 2:
        return True
    return False



def reverse_commands(commands_list):
    """
    Reverses a list of commands.

    Args:
        command_list: A list of strings representing commands.

    Returns:
        _: A reversed list of strings representing commands.
    """

    return commands_list[::-1]


def limit_range(command_list, limit):
    """
    Limit the range of commands replayed.

    Args:
        command_list: A list of strings representing movement commands.
        limit: A string representing the limiting range.

    Returns:
        _: A limited list of strings representing movement commands.
    """

    if len(limit.split("-")) == 1 and limit.isdigit():
        return command_list[-int(limit):]
    if len(limit.split("-")) == 2:
        upper_limit = -int(limit.split("-")[0])
        lower_limit = -int(limit.split("-")[1])
        return command_list[upper_limit:lower_limit]
    else:
        return command_list


def replay_commands(robot, limit="", silent_mode=False, reverse_mode=False):
    """
    Replays the movement commands in the command history.

    Args:
        robot: A dictionary that represents the robots attributes.

    Returns:
        robot: A dictionary that represents the robots attributes.
    """

    command_list = retrieve_movement_commands(robot)

    if reverse_mode:
        command_list = reverse_commands(command_list)
        robot["reverse_mode"] = reverse_mode
    if silent_mode:
        robot["silent_mode"] = silent_mode

    command_list = limit_range(command_list, limit)
    for command in command_list:
        execute_command(robot, command)
        robot["command_history"] = robot["command_history"][:-1]

    world.display_robot_replay(robot, len(command_list))
    return robot


def find_limit(command):
    """
    Finds and extracts the limiting range of a replay command.

    Args:
        command: A string representing the currnet command.

    Returns:
        _: A string representing the limiting range of a replay command.
    """

    command = command.strip().split()
    replay_commands = ["replay", "silent", "reversed"]
    if len(command) < 2 or len(command) > 4:
        return ""

    limit_list = list(filter(lambda x: contains_digit(x), command[1:]))
    valid_commands = list(filter(lambda x: True if x in replay_commands or contains_digit(x) else False, command))

    if command[0] == "replay" and len(limit_list) == 1 and len(command) == len(valid_commands):
        return limit_list[0]
    return ""


def execute_command(robot, command):
    """
    Executes valid user commands.

    Args:
        robot: A dictionary that represents the robots attributes.
        command: A string representing the command to be executed.

    Return:
        robot: A dictionary that represents the robots attributes.
    """

    robot = add_command_to_history(robot, command)

    if command == "off":
        display_shut_down(robot["name"])
    elif command == "help":
        display_help()
    elif "forward" in command:
        robot = move_forward(robot, command)
        world.display_robot_position(robot)
    elif "back" in command:
        robot = move_back(robot, command)
        world.display_robot_position(robot)
    elif command in ["left", "right"]:
        robot = turn(robot, command)
        world.display_robot_position(robot)
    elif "sprint" in command:
        robot = sprint(robot, command)
        world.display_robot_position(robot)
    elif "replay" in command:
        silent_mode=activate_silent_mode(command)
        reverse_mode=activate_reverse_mode(command)
        limit = find_limit(command)
        robot = replay_commands(robot, limit, silent_mode, reverse_mode)
        world.display_robot_position(robot)
    elif "mazerun" in command:
        if len(command.split()) == 2 and command.split()[1] in ["top","bottom","left", "right"]:
            border = command.split()[1]
        else:
            border = "top"
        robot = run_maze(robot, border)
        world.display_robot_position(robot)
    return robot


def create_robot():
    """
    Creates a dictionary that contains information about a robot.

    Args:
        N/A

    Returns:
        _: A dictionary representing name, direction and position of the robot.
    """

    return {"name": "", "position_x": 0, "position_y": 0, "direction":"N", "command_history":[]}


def dummy_obstacles():
    """
    Randomy creates a random number of coordinates that act as dummies.

    Args:
        N/A

    Returns:
        obstacles: A list of tuples.
    """

    obstacles = []
    number_of_obstacles = random.randint(1, 10)
    if number_of_obstacles == 0:
        return obstacles
    for _ in range(1, number_of_obstacles + 1):
        obstacle = (random.randint(-300, 300), random.randint(-300, 300))
        obstacles.append(obstacle)
        return obstacles


def robot_start_display(robot):
    if maze and "unittest" not in sys.modules.keys():
        robot_response(robot["name"], f"Loaded {sys.argv[2]}")
    if "world.text.world" in sys.modules:
        world.obstacles.global_obstacles = dummy_obstacles() 
        robot_response(robot['name'], "Loaded obstacles.")
        world.display_obstacles()


def add_direction_tracker(robot):
    """
    Adds the ability to track a robots direction during a maze run.

    Args:
        robot: A dictionary representing the robot state.

    Reterns:
        robot: A dictionary representing the robot state.
    """

    robot["direction_tracker"] = []
    return robot


def mazerun_move(robot):
    """
    Moves the mazerunner forward by a single step.

    Args:
        robot: A dictionary representing the robot state.

    Returns:
        robot: A dictionary representing the robot state.
    """
    
    return execute_command(robot, "forward 1")


def successful_move(robot_one, robot_two):
    """
    Checks if a move was successful by comparing the original robot with the result.

    Args:
        robot_one: A dictionary representing the original robot state.
        robot_two: A dictionary representing the result robot state.

    Returns:
        _: A bool indicating if a move was successful i.e the robots are different.
    """

    if robot_one != robot_two:
        return True
    return False


def run_maze(robot, border):
    """
    Starts a maze run

    Args:
        robot: A dictionary representing the robot state.
        border: A string indicating which side of the maze the robot should go.

    return:
        robot: A dictionary representing the robot state.
    """

    if maze:
        maze.display_maze_runner(robot)
    robot = add_direction_tracker(robot)
    turn_map = {"right":1, "bottom":2, "left":3, "top":0}
    for _ in range(0,turn_map[border]):
        execute_command(robot, "right")
    while(True):
        robot_two = mazerun_move(robot.copy())
        if successful_move(robot, robot_two):
            del robot
            robot = robot_two
            if len(robot["direction_tracker"]) > 0:
                execute_command(robot, "left")
                robot["direction_tracker"].pop()
        else:
            if world.on_boundary(robot, border):
                robot_response(robot["name"], f"I am at the {border} edge.")
                break
            del robot_two
            execute_command(robot, "right")
            robot["direction_tracker"].append("left")
    return robot


def robot_start():
    """This is the entry function, do not change"""

    robot = create_robot()
    robot["name"] = get_robot_name()
    robot_response(robot["name"], "Hello kiddo!")
    robot_start_display(robot)
    command = get_command(robot["name"])
    while(command.lower() != "off"):
        robot = execute_command(robot, command)
        command = get_command(robot["name"])
    display_shut_down(robot["name"])
    pass


if __name__ == "__main__":
    robot_start()
