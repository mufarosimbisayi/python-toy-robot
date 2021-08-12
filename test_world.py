import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.text.world as world


class MyTestCase(unittest.TestCase):

    def test_within_limit_true(self):
        self.assertTrue(world.within_limit({"name":"HAL", "position_x":60, "position_y":70, "direction":"E"}))
        self.assertTrue(world.within_limit({"name":"HAL", "position_x":60, "position_y":70, "direction":"W"}))
        self.assertTrue(world.within_limit({"name":"HAL", "position_x":60, "position_y":70, "direction":"N"}))
        self.assertTrue(world.within_limit({"name":"HAL", "position_x":60, "position_y":70, "direction":"S"}))


    def test_within_limit_false(self):
        self.assertFalse(world.within_limit({"name":"HAL", "position_x":1600, "position_y":70, "direction":"E"}))
        self.assertFalse(world.within_limit({"name":"HAL", "position_x":-1600, "position_y":70, "direction":"W"}))
        self.assertFalse(world.within_limit({"name":"HAL", "position_x":600, "position_y":700, "direction":"N"}))
        self.assertFalse(world.within_limit({"name":"HAL", "position_x":600, "position_y":-270, "direction":"S"}))
        

    def test_display_robot_movement_forward(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_movement({"name":"Kitty"}, "forward 10")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > Kitty moved forward by 10 steps.""")


    def test_display_robot_movement_back(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_movement({"name":"HAL"}, "back 14")
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL moved back by 14 steps.""")


    def test_display_robot_position(self):
        with captured_io(StringIO()) as (out, err):
            toy_robot = {"name":"HAL", "position_x":0, "position_y":15, "direction":"E"}
            world.display_robot_position(toy_robot)
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", """ > HAL now at position (0,15).""")


    def test_display_robot_replay(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_replay({"name":"HAL"}, 6)
        output = out.getvalue().strip()
        self.assertEqual(output, """> HAL replayed 6 commands.""")


    def test_display_robot_replay_silent(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_replay({"name":"HAL", "silent_mode":True}, 6)
        output = out.getvalue().strip()
        self.assertEqual(output, """> HAL replayed 6 commands silently.""")


    def test_display_robot_replay_reversed(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_replay({"name":"HAL", "reverse_mode": True}, 6)
        output = out.getvalue().strip()
        self.assertEqual(output, """> HAL replayed 6 commands in reverse.""")


    def test_display_robot_replay_reversed_silently(self):
        with captured_io(StringIO()) as (out, err):
            world.display_robot_replay({"name":"HAL", "silent_mode":True, "reverse_mode":True}, 6)
        output = out.getvalue().strip()
        self.assertEqual(output, """> HAL replayed 6 commands in reverse silently.""")


    def test_display_obstacles(self):
        with captured_io(StringIO()) as (out, err):
            world.obstacles.global_obstacles = [(1,1), (7,9)]
            world.display_obstacles()
        output = out.getvalue().strip()
        self.assertEqual(output, """There are some obstacles:
- At position 1,1 (to 5,5)
- At position 7,9 (to 11,13)""")


    def test_encounters_obstacles_true(self):
        world.obstacles.global_obstacles = [(1,1)]
        self.assertTrue(world.obstacles.is_path_blocked(3,0,3,7))
        self.assertTrue(world.obstacles.is_path_blocked(10,3,3,3))


    def test_encounters_obstacles_false(self):
        world.obstacles.global_obstacles = [(1,1)]
        self.assertFalse(world.obstacles.is_path_blocked(0,0,0,7))
        self.assertFalse(world.obstacles.is_path_blocked(10,7,3,7))
