import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.obstacles as obstacles


class MyTestCase(unittest.TestCase):

    def test_create_obstacles(self):
        obstacles.random.randint = lambda a, b: 1
        self.assertEqual(obstacles.create_obstacles(), [(1,1)])


    def test_is_position_blocked_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.is_position_blocked(2,2))
        self.assertTrue(obstacles.is_position_blocked(1,5))
        self.assertTrue(obstacles.is_position_blocked(5,1))
        self.assertTrue(obstacles.is_position_blocked(4,2))


    def test_is_position_blocked_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.is_position_blocked(1,6))
        self.assertFalse(obstacles.is_position_blocked(6,1))
        self.assertFalse(obstacles.is_position_blocked(2,8))
        self.assertFalse(obstacles.is_position_blocked(38,4))


    def test_is_in_range_true(self):
        self.assertTrue(obstacles.is_in_range(1, 1))
        self.assertTrue(obstacles.is_in_range(1, 2))
        self.assertTrue(obstacles.is_in_range(1, 5))


    def test_is_in_range_false(self):
        self.assertFalse(obstacles.is_in_range(1, 0))
        self.assertFalse(obstacles.is_in_range(1, 6))


    def test_is_path_blocked_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.is_path_blocked(0,1,2,1))
        self.assertTrue(obstacles.is_path_blocked(1,0,1,2))


    def test_is_path_blocked_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.is_path_blocked(2,6,6,4))


    def test_get_obstacles(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertEqual(obstacles.get_obstacles(), [(1,1)])

