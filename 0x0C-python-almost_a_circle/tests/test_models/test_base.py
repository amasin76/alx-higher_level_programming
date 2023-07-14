import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class"""

    def setUp(self):
        """Method that runs before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for the id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)
