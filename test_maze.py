import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.maze.mufaros_maze as obstacles


class MyTestCase(unittest.TestCase):

    def test_create_obstacles(self):
        obstacles.random.randint = lambda a, b: 1
        self.assertEqual(obstacles.create_obstacles(), [(1,1)])


    def test_is_position_blocked_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.is_position_blocked(1,1))
        self.assertTrue(obstacles.is_position_blocked(1,5))
        self.assertTrue(obstacles.is_position_blocked(1,11))
        self.assertTrue(obstacles.is_position_blocked(1,20))
        self.assertTrue(obstacles.is_position_blocked(4,20))
        self.assertTrue(obstacles.is_position_blocked(8,20))


    def test_is_position_blocked_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.is_position_blocked(2,6))
        self.assertFalse(obstacles.is_position_blocked(2,1))
        self.assertFalse(obstacles.is_position_blocked(0,6))
        self.assertFalse(obstacles.is_position_blocked(0,1))
        self.assertFalse(obstacles.is_position_blocked(1,21))
        self.assertFalse(obstacles.is_position_blocked(9,20))
        self.assertFalse(obstacles.is_position_blocked(0,20))


    def test_create_obstacle_list(self):
        self.assertEqual(obstacles.create_obstacle_list((1,1)),[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(2,20),(3,20),(4,20),(5,20),(6,20),(7,20),(8,20)])
        self.assertEqual(obstacles.create_obstacle_list((-4,15)),[(-4,15),(-4,16),(-4,17),(-4,18),(-4,19),(-4,20),(-4,21),(-4,22),(-4,23),(-4,24),(-4,25),(-4,26),(-4,27),(-4,28),(-4,29),(-4,30),(-4,31),(-4,32),(-4,33),(-4,34),(-3,34),(-2,34),(-1,34),(0,34),(1,34),(2,34),(3,34)])


    def test_in_obstacle_list_true(self):
        self.assertTrue(obstacles.in_obstacle_list((5,20),(1,1)))
        self.assertTrue(obstacles.in_obstacle_list((0,34),(-4,15)))


    def test_in_obstacle_list_false(self):
        self.assertFalse(obstacles.in_obstacle_list((5,11),(1,1)))
        self.assertFalse(obstacles.in_obstacle_list((0,35),(-4,15)))

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

