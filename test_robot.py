import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot


class MyTestCase(unittest.TestCase):

    def test_get_robot_name(self):
        with captured_io(StringIO('Kitty\n')) as (out, err):
            returns = robot.get_robot_name()
        output= out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot?""")
        self.assertEqual(returns, "Kitty")

    def test_robot_response(self):
        with captured_io(StringIO()) as (out, err):
            robot.robot_response("Kitty", "Hello kiddo!")
        output = out.getvalue().strip()
        self.assertEqual(output, """Kitty: Hello kiddo!""")


    def test_valid_command_true(self):
        self.assertTrue(robot.valid_command("Replay"))
        self.assertTrue(robot.valid_command("Forward 10"))
        self.assertTrue(robot.valid_command("back 2"))


    def test_valid_command_false(self):
        self.assertFalse(robot.valid_command("False"))
        self.assertFalse(robot.valid_command("true"))


    def test_valid_command_with_steps_true(self):
        self.assertTrue(robot.valid_command("sprint 23"))
        self.assertTrue(robot.valid_command("replay 1"))
        self.assertTrue(robot.valid_command("back 0"))


    def test_valid_command_false(self):
        self.assertFalse(robot.valid_command("False 12"))
        self.assertFalse(robot.valid_command("false 0"))


    def test_get_command_valid(self):
        with captured_io(StringIO("off\n")) as (out, err):
            returns = robot.get_command("HAL")
        output = out.getvalue().strip()
        self.assertEqual(returns, "off")
        self.assertEqual(output, """HAL: What must I do next?""")


    def test_get_command_invalid(self):
        with captured_io(StringIO("Jump\noff\n")) as (out, err):
            robot.get_command("HAL")
        output = out.getvalue().strip()
        self.assertEqual(output, """HAL: What must I do next? HAL: Sorry, I did not understand 'Jump'.\nHAL: What must I do next?""")


    def test_display_shut_down(self):
        with captured_io(StringIO()) as (out, err):
            robot.display_shut_down("Kitty")
        output = out.getvalue().strip()
        self.assertEqual(output, "Kitty: Shutting down..")


    def test_execute_command_off(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"HAL","position_x":5, "position_y":0, "command_history":[]}
            robot.execute_command(toy_robot, "off")
        output = out.getvalue().strip()
        self.assertEqual(output, "HAL: Shutting down..")

    def test_display_help(self):
        with captured_io(StringIO()) as (out, err):
            robot.display_help()
        output = out.getvalue().strip()
        self.assertEqual(output, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
REPLAY - redo all the movement commands""")


    def test_execute_command_help(self):
        toy_robot = {"name":"HAL","position_x":5, "position_y":0, "command_history":[]}
        with captured_io(StringIO()) as (out, err):
            robot.execute_command(toy_robot, "help")
        output = out.getvalue().strip()
        self.assertEqual(output, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
REPLAY - redo all the movement commands""")       


    def test_move_forward_north(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"N"}
            robot.move_forward(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved forward by 10 steps.""")


    def test_move_forward_south(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"S"}
            robot.move_forward(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved forward by 10 steps.""")


    def test_move_forward_east(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"E"}
            robot.move_forward(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved forward by 10 steps.""")       


    def test_move_forward_west(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"W"}
            robot.move_forward(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved forward by 10 steps.""")


    def test_execute_command_move_forward(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"HAL", "position_x":0, "position_y":5, "direction":"N", "command_history":[]}
            robot.execute_command(toy_robot, "forward 13")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved forward by 13 steps.
 > HAL now at position (0,18).""")


    def test_create_robot(self):
        self.assertEqual(robot.create_robot(), {"name":"", "position_x":0, "position_y":0, "direction":"N", "command_history":[]})


    def test_move_back_north(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"N"}
            robot.move_back(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved back by 10 steps.""")


    def test_move_back_south(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"S"}
            robot.move_back(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved back by 10 steps.""")


    def test_move_back_east(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"E"}
            robot.move_back(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved back by 10 steps.""")


    def test_move_back_west(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"Kitty","position_x":5, "position_y":0, "direction":"W"}
            robot.move_back(toy_robot, "10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved back by 10 steps.""")



    def test_execute_command_move_back(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"HAL", "position_x":0, "position_y":15, "direction":"N", "command_history":[]}
            robot.execute_command(toy_robot, "back 13")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved back by 13 steps.
 > HAL now at position (0,2).""")


    def test_turn_right(self):
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"N"}, "right"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"W"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"W"}, "right"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"S"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}, "right"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"N"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"S"}, "right"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E"})


    def test_turn_left(self):
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"S"}, "left"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"W"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"N"}, "left"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"W"}, "left"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"N"})
        self.assertEqual(robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}, "left"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"S"})


    def test_execute_command_turn(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "left"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"S", "command_history": ["left"]})


    def test_turn_left_output(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}, "left")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL turned left.""")


    def test_turn_right_output(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}, "right")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL turned right.""")


    def test_turn_left_output(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = robot.turn({"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}, "left")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL turned left.""")


    def test_move_back_limit_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.move_back({"name":"HAL", "position_x":60, "position_y":100, "direction":"S"}, "1000")
        output = out.getvalue().strip()
        self.assertEqual(output, """HAL: Sorry, I cannot go outside my safe zone.""")


    def test_move_forward_limit_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.move_forward({"name":"HAL", "position_x":60, "position_y":100, "direction":"N"}, "1000")
        output = out.getvalue().strip()
        self.assertEqual(output, """HAL: Sorry, I cannot go outside my safe zone.""")


    def test_sprint(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}
            robot.sprint(toy_robot, "sprint 3")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.""")


    def test_execute_command_sprint(self):
        toy_robot = {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}
        sprint_robot = {"name":"HAL", "position_x":-6, "position_y":15, "direction":"E", "command_history":["sprint 3"]}
        self.assertEqual(robot.execute_command(toy_robot, "sprint 3"), sprint_robot)


    def test_add_command_to_history(self):
        toy_robot = {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}
        self.assertEqual(robot.add_command_to_history(toy_robot, "forward 10"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]})
        self.assertEqual(robot.add_command_to_history(toy_robot, "help"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help"]})


    def test_retrieve_command_history(self):
        self.assertEqual(robot.retrieve_command_history({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}), [])
        self.assertEqual(robot.retrieve_command_history({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}), ["forward 10"])
        self.assertEqual(robot.retrieve_command_history({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}), ["forward 10", "back 5"])


    def test_replay_commands(self):
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}), {"name":"HAL", "position_x":-10, "position_y":20, "direction":"S", "command_history":["forward 10", "left", "back 5"]})


    def test_replay_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]})
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved forward by 10 steps.
 > HAL now at position (-10,15).
 > HAL moved back by 5 steps.
 > HAL now at position (-5,15).
 > HAL replayed 2 commands.""")


    def test_retrieve_movement_commands(self):
        self.assertEqual(robot.retrieve_movement_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}), [])
        self.assertEqual(robot.retrieve_movement_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}), ["forward 10"])
        self.assertEqual(robot.retrieve_movement_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}), ["forward 10", "back 5"])
        self.assertEqual(robot.retrieve_movement_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "help","left"]}), ["forward 10", "left"])


    def test_execute_command_replay(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay"),{"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["replay"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, "replay"), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10", "replay"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, "replay"), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5", "replay"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, "replay"), {"name":"HAL", "position_x":-10, "position_y":20, "direction":"S", "command_history":["forward 10", "left", "back 5", "replay"]})


    def test_execute_command_replay_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, "replay")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved forward by 10 steps.
 > HAL now at position (-10,15).
 > HAL moved back by 5 steps.
 > HAL now at position (-5,15).
 > HAL replayed 2 commands.
 > HAL now at position (-5,15).""")


    def test_execute_command_replay_empty_history_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 0 commands.
 > HAL now at position (0,15).""")


    def test_replay_silent_commands(self):
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, silent_mode=True), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, silent_mode=True), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, silent_mode=True), {"name":"HAL", "position_x":-10, "position_y":20, "direction":"S", "command_history":["forward 10", "left", "back 5"]})


    def test_replay_silent_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, silent_mode=True)
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 2 commands silently.""")


    def test_execute_command_replay_silent(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay silent"),{"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["replay silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, "replay silent"), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10", "replay silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, "replay silent"), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5", "replay silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, "replay silent"), {"name":"HAL", "position_x":-10, "position_y":20, "direction":"S", "command_history":["forward 10", "left", "back 5", "replay silent"]})


    def test_execute_command_replay_silent_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, "replay silent")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 2 commands silently.
 > HAL now at position (-5,15).""")


    def test_execute_command_replay_silent_empty_history_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay silent")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 0 commands silently.
 > HAL now at position (0,15).""")


    def test_activate_silent_mode_true(self):
        self.assertTrue(robot.activate_silent_mode("replay silent"))
        self.assertTrue(robot.activate_silent_mode("replay reversed silent"))


    def test_activate_silent_mode_false(self):
        self.assertFalse(robot.activate_silent_mode("replay"))
        self.assertFalse(robot.activate_silent_mode("silent"))
        self.assertFalse(robot.activate_silent_mode("W"))
        self.assertFalse(robot.activate_silent_mode("replay silnt"))
        self.assertFalse(robot.activate_silent_mode("repay silent"))
        self.assertFalse(robot.activate_silent_mode(""))


    def test_activate_reverse_mode_true(self):
        self.assertTrue(robot.activate_reverse_mode("replay reversed"))
        self.assertTrue(robot.activate_reverse_mode("replay reversed silent"))


    def test_activate_reverse_mode_false(self):
        self.assertFalse(robot.activate_reverse_mode("replay"))
        self.assertFalse(robot.activate_reverse_mode("reversed"))
        self.assertFalse(robot.activate_reverse_mode("W"))
        self.assertFalse(robot.activate_reverse_mode("replay reverse"))
        self.assertFalse(robot.activate_reverse_mode("repay reversed"))
        self.assertFalse(robot.activate_reverse_mode(""))



    def test_replay_commands_reversed(self):
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, reverse_mode=True), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, reverse_mode=True), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, reverse_mode=True), {"name":"HAL", "position_x":5, "position_y":5, "direction":"S", "command_history":["forward 10", "left", "back 5"]})


    def test_replay_reverse_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, reverse_mode=True)
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved back by 5 steps.
 > HAL now at position (5,15).
 > HAL moved forward by 10 steps.
 > HAL now at position (-5,15).
 > HAL replayed 2 commands in reverse.""")


    def test_execute_command_replay(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay reversed"),{"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["replay reversed"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, "replay reversed"), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10", "replay reversed"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, "replay reversed"), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5", "replay reversed"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, "replay reversed"), {"name":"HAL", "position_x":5, "position_y":5, "direction":"S", "command_history":["forward 10", "left", "back 5", "replay reversed"]})


    def test_execute_command_replay_reversed_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, "replay reversed")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved back by 5 steps.
 > HAL now at position (5,15).
 > HAL moved forward by 10 steps.
 > HAL now at position (-5,15).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (-5,15).""")


    def test_execute_command_replay_reversed_empty_history_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay reversed")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 0 commands in reverse.
 > HAL now at position (0,15).""")


    def test_reverse_commands(self):
        self.assertEqual(robot.reverse_commands(["forward 10", "back 5"]), ["back 5", "forward 10"])


    def test_replay_commands_reversed_silent(self):
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, reverse_mode=True, silent_mode=True), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, reverse_mode=True, silent_mode=True), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]})
        self.assertEqual(robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, reverse_mode=True, silent_mode=True), {"name":"HAL", "position_x":5, "position_y":5, "direction":"S", "command_history":["forward 10", "left", "back 5"]})


    def test_replay_reverse_silent_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.replay_commands({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, reverse_mode=True, silent_mode=True)
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 2 commands in reverse silently.""")


    def test_execute_command_replay_reversed_silent(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay reversed silent"),{"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["replay reversed silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10"]}, "replay reversed silent"), {"name":"HAL", "position_x":-10, "position_y":15, "direction":"E", "command_history":["forward 10", "replay reversed silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5"]}, "replay reversed silent"), {"name":"HAL", "position_x":-5, "position_y":15, "direction":"E", "command_history":["forward 10", "back 5", "replay reversed silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","left", "back 5"]}, "replay reversed silent"), {"name":"HAL", "position_x":5, "position_y":5, "direction":"S", "command_history":["forward 10", "left", "back 5", "replay reversed silent"]})


    def test_execute_command_replay_reversed_silent_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["forward 10","help", "back 5"]}, "replay reversed silent")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 2 commands in reverse silently.
 > HAL now at position (-5,15).""")


    def test_execute_command_replay_reversed_silent_empty_history_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":[]}, "replay reversed silent")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL replayed 0 commands in reverse silently.
 > HAL now at position (0,15).""")


    def test_limit_range_unbound(self):
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "2"), ["left", "right"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "2"), ["left", "right"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "2"), ["left", "right"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "2"), ["left", "right"])


    def test_limit_range_bound(self):
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "3-1"), ["right", "left"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "3-1"), ["right", "left"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "3-1"), ["right", "left"])
        self.assertEqual(robot.limit_range(["left", "right", "left", "right"], "3-1"), ["right", "left"])


    def test_limit_range_used(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay 1"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"N", "command_history":["left", "right", "left", "right", "replay 1"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay silent 2"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right", "replay silent 2"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay reversed 3"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"S", "command_history":["left", "right", "left", "right", "replay reversed 3"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay reversed silent 3"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"S", "command_history":["left", "right", "left", "right", "replay reversed silent 3"]})


    def test_limit_range_unused(self):
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right", "replay"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay silent"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right", "replay silent"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay reversed"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right", "replay reversed"]})
        self.assertEqual(robot.execute_command({"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right"]}, "replay reversed silent"), {"name":"HAL", "position_x":0, "position_y":15, "direction":"E", "command_history":["left", "right", "left", "right", "replay reversed silent"]})


    def test_valid_command_list(self):
        self.assertEqual(robot.valid_command_list(), ["forward", "back", "left", "right", "sprint", "replay", "reversed", "silent", "help", "off"])


    def test_contains_digit_true(self):
        self.assertTrue(robot.contains_digit("4"))
        self.assertTrue(robot.contains_digit("4-1"))


    def test_contains_digit_false(self):
        self.assertFalse(robot.contains_digit("4e"))
        self.assertFalse(robot.contains_digit("4.5"))
        self.assertFalse(robot.contains_digit("4,5"))
        self.assertFalse(robot.contains_digit("4:5"))
        self.assertFalse(robot.contains_digit("g"))
        self.assertFalse(robot.contains_digit("Hello"))
        self.assertFalse(robot.contains_digit("4)5"))
        self.assertFalse(robot.contains_digit("4_5"))


    def test_find_limit_true(self):
        self.assertEqual(robot.find_limit("replay 4"), "4")
        self.assertEqual(robot.find_limit("replay 4-2"), "4-2")
        self.assertEqual(robot.find_limit("replay silent 4"), "4")
        self.assertEqual(robot.find_limit("replay reversed silent 4-2"), "4-2")
        self.assertEqual(robot.find_limit("replay 4 reversed"), "4")
        self.assertEqual(robot.find_limit("replay 4-2 reversed silent"), "4-2")


    def test_find_limit_false(self):
        self.assertEqual(robot.find_limit("replay"), "")
        self.assertEqual(robot.find_limit("replayd 4-2"), "")
        self.assertEqual(robot.find_limit("replay slent 4"), "")
        self.assertEqual(robot.find_limit("replay reversd silent 4-2"), "")
        self.assertEqual(robot.find_limit("replay 4x reversed"), "")
        self.assertEqual(robot.find_limit("replay 4-r2 reversed silent"), "")


    def test_dummy_obstacles(self):
        robot.random.randint = lambda a,b: 1
        self.assertEqual(robot.dummy_obstacles(), [(1,1)])


    def test_check_obstacles_true(self):
        robot_two = {"position_x":0, "position_y":-80, "name":"HAL"}
        robot_one = {"position_x":0, "position_y":-120}
        self.assertTrue(robot.check_obstacles(robot_one, robot_two))


    def test_check_obstacles_false(self):
        robot_two = {"position_x":0, "position_y":-180, "name":"HAL"}
        robot_one = {"position_x":0, "position_y":-220}
        self.assertFalse(robot.check_obstacles(robot_one, robot_two))


    def test_check_limit_true(self):
        robot_one = {"position_x":320, "position_y":-80, "name":"HAL"}
        self.assertTrue(robot.check_limit(robot_one))


    def test_check_limit_false(self):
        robot_one = {"position_x":0, "position_y":-180, "name":"HAL"}
        self.assertFalse(robot.check_limit(robot_one))

