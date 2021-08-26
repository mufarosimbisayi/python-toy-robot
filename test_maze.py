import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.maze.mufaros_maze as maze


class MyTestCase(unittest.TestCase):

    def test_is_position_blocked_true(self):
        maze.global_maze = maze.create_inner_maze()
        self.assertTrue(maze.is_position_blocked(-80,-100))
        self.assertTrue(maze.is_position_blocked(80,-100))
        self.assertTrue(maze.is_position_blocked(0,-100))
        self.assertTrue(maze.is_position_blocked(100,-80))
        self.assertTrue(maze.is_position_blocked(100,80))
        self.assertTrue(maze.is_position_blocked(100,0))
        self.assertTrue(maze.is_position_blocked(80,100))
        self.assertTrue(maze.is_position_blocked(-80,100))
        self.assertTrue(maze.is_position_blocked(0,100))
        self.assertTrue(maze.is_position_blocked(-100,80))
        self.assertTrue(maze.is_position_blocked(-100,-80))
        self.assertTrue(maze.is_position_blocked(-100,0))


    def test_is_position_blocked_false(self):
        maze.global_maze = maze.create_inner_maze()
        self.assertFalse(maze.is_position_blocked(-100,-100))
        self.assertFalse(maze.is_position_blocked(100,-100))
        self.assertFalse(maze.is_position_blocked(100,100))
        self.assertFalse(maze.is_position_blocked(-100,100))



    def test_create_inner_maze_true(self):
        self.assertTrue(set([(-80,-100), (80,-100)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(100,-80), (100,80)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(80,100), (-80,100)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(-100,80), (-100,-80)]) <= set(maze.create_inner_maze()))


    def test_create_inner_maze_false(self):
        self.assertFalse(set([(-100,-100)]) <= set(maze.create_inner_maze()))
        self.assertFalse(set([(100,-100)]) <= set(maze.create_inner_maze()))
        self.assertFalse(set([(100,100)]) <= set(maze.create_inner_maze()))
        self.assertFalse(set([(-100,100)]) <= set(maze.create_inner_maze()))


    def test_create_outer_maze(self):
        self.assertTrue(set([(-200,-200), (-20,-200)]) <= set(maze.create_outer_maze()))
        self.assertTrue(set([(20,-200), (200,-200)]) <= set(maze.create_outer_maze()))
        self.assertTrue(set([(200,-20), (200,20)]) <= set(maze.create_outer_maze()))
        self.assertTrue(set([(200,200), (20,200)]) <= set(maze.create_outer_maze()))
        self.assertTrue(set([(-20,200), (-200,200)]) <= set(maze.create_outer_maze()))
        self.assertTrue(set([(-200,20), (-200,-20)]) <= set(maze.create_outer_maze()))


    def test_create_outer_maze_false(self):
        self.assertFalse(set([(0,-200)]) <= set(maze.create_outer_maze()))
        self.assertFalse(set([(200,0)]) <= set(maze.create_outer_maze()))
        self.assertFalse(set([(0,200)]) <= set(maze.create_outer_maze()))
        self.assertFalse(set([(-200,0)]) <= set(maze.create_outer_maze()))


    def test_is_path_blocked_true(self):
        maze.global_maze = [(1,1)]
        self.assertTrue(maze.is_path_blocked(0,1,2,1))
        self.assertTrue(maze.is_path_blocked(1,0,1,2))


    def test_is_path_blocked_false(self):
        maze.global_maze = [(1,1)]
        self.assertFalse(maze.is_path_blocked(2,6,6,4))


    def test_get_maze(self):
        maze.global_maze = [(1,1)]
        self.assertEqual(maze.get_maze(), [(1,1)])


    def test_display_maze_runner(self):
        with captured_io(StringIO()) as (out, err):
            maze.display_maze_runner({"name":"HAL"})
        output = out.getvalue().strip()
        self.assertEqual(f" {output}", " > HAL starting maze run..")
