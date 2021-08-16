import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.maze.mufaros_maze as obstacles


class MyTestCase(unittest.TestCase):

    def test_create_obstacles(self):
        obstacles.random.randint = lambda a, b: 1
        self.assertEqual(obstacles.create_obstacles(-300,-300,300,300), [(1,1)])


    def test_is_position_blocked_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.is_position_blocked(1,1))
        self.assertTrue(obstacles.is_position_blocked(1,50))
        self.assertTrue(obstacles.is_position_blocked(1,110))
        self.assertTrue(obstacles.is_position_blocked(1,200))
        self.assertTrue(obstacles.is_position_blocked(45,200))
        self.assertTrue(obstacles.is_position_blocked(90,200))


    def test_is_position_blocked_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.is_position_blocked(2,50))
        self.assertFalse(obstacles.is_position_blocked(2,100))
        self.assertFalse(obstacles.is_position_blocked(0,60))
        self.assertFalse(obstacles.is_position_blocked(0,100))
        self.assertFalse(obstacles.is_position_blocked(1,210))
        self.assertFalse(obstacles.is_position_blocked(95,200))
        self.assertFalse(obstacles.is_position_blocked(0,200))


    def test_create_obstacle_list(self):
        self.assertEqual(len(obstacles.create_obstacle_list((1,1))),289)


    def test_obstacle_cross_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.obstacles_cross((45,90),(1,1)))


    def test_obstacle_cross_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.obstacles_cross((0,90),(1,1)))


    def test_oll_0bstacles_cross_true(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertTrue(obstacles.all_obstacles_cross((45,90)))


    def test_all_obstacles_cross_false(self):
        obstacles.global_obstacles = [(1,1)]
        self.assertFalse(obstacles.all_obstacles_cross((0,90)))



    def test_in_obstacle_list_true(self):
        self.assertTrue(obstacles.in_obstacle_list((1,105),(1,1)))
        self.assertTrue(obstacles.in_obstacle_list((6,214),(-4,15)))


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

