import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.maze.mufaros_maze as maze


class MyTestCase(unittest.TestCase):

    def test_create_inner_maze(self):
        self.assertTrue(set([(-80,-100), (80,-100)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(100,-80), (100,80)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(80,100), (-80,100)]) <= set(maze.create_inner_maze()))
        self.assertTrue(set([(-100,80), (-100,-80)]) <= set(maze.create_inner_maze()))


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

