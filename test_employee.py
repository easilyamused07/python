#11-3
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee.py"""
    
    def setUp(self):
        self.employee = Employee('carla','ramirez',100000)
    
    def test_default_raise(self):
        """Does default raise work?"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,105000)
        
    def test_custom_raise(self):
        """Does custom raise work?"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,110000)
        
unittest.main()
