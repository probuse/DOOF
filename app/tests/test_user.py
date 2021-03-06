import unittest
from app.user import User
from app.category import Category


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Adrian", "adris", "secret")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    
    def test_add_category_None(self):
         self.assertEqual(self.user.add_category(None), "None input")

    def test_add_category_blank_input(self):
        self.assertEqual(self.user.add_category(" "), "Blank input")

    def test_add_category_should_be_between10and60(self):
        self.assertEqual(self.user.add_category("shortname"),
                         "category name should be greater than 10 and less than 60 characters")

        self.assertEqual(self.user.add_category("long name long name long name long name long name long name long name"),
                         "category name should be greater than 10 and less than 60 characters")

    def test_add_category_added(self):
        self.assertEqual(self.user.add_category("Appetizers"),
                         "category added")
                     
    def test_add_category_name_already_exists(self):
        self.user.add_category("Appetizers")
        self.assertEqual(self.user.add_category
                         ("Appetizers"),
                         "An category with this name already exists")
