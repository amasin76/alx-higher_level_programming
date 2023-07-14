import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class"""

    def setUp(self):
        """Method that runs before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for the id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Test for the width attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

        r.width = 20
        self.assertEqual(r.width, 20)

    def test_height(self):
        """Test for the height attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

        r.height = 4
        self.assertEqual(r.height, 4)

    def test_x(self):
        """Test for the x attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)

        r.x = 1
        self.assertEqual(r.x, 1)

    def test_y(self):
        """Test for the y attribute"""
        r = Rectangle(10, 2)
        self.assertEqual(r.y, 0)

        r.y = 1
        self.assertEqual(r.y, 1)
