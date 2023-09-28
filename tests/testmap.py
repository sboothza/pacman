import unittest
from map import Map, Point


class MapTests(unittest.TestCase):

    def setUp(self):
        self.map = Map()
        node_a = self.map.add_node(50, 100)
        node_b = self.map.add_node(600, 100)
        node_c = self.map.add_node(600, 600)
        node_d = self.map.add_node(50, 600)
        self.map.add_path(node_a, node_b, "a-b")
        self.map.add_path(node_b, node_c, "b-c")
        self.map.add_path(node_c, node_d, "c-d")
        self.map.add_path(node_d, node_a, "d-a")

    def test_find_node(self):
        node = self.map.find_node(Point(50, 100))
        self.assertIsNotNone(node)
        node = self.map.find_node(Point(600, 100))
        self.assertIsNotNone(node)
        node = self.map.find_node(Point(600, 600))
        self.assertIsNotNone(node)
        node = self.map.find_node(Point(50, 600))
        self.assertIsNotNone(node)

    def test_find_path(self):
        path = self.map.find_path(Point(51, 100))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "a-b")
        path = self.map.find_path(Point(599, 100))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "a-b")
        path = self.map.find_path(Point(600, 101))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "b-c")
        path = self.map.find_path(Point(600, 599))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "b-c")
        path = self.map.find_path(Point(599, 600))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "c-d")
        path = self.map.find_path(Point(51, 600))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "c-d")
        path = self.map.find_path(Point(50, 599))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "d-a")
        path = self.map.find_path(Point(50, 101))
        self.assertIsNotNone(path)
        self.assertEqual(path.name, "d-a")

    def test_move(self):
