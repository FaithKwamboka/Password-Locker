import unittest
from credentials import Credential


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Credential("Facebook", "Faith", "Kwamboka@")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.account_name, "Facebook")
        self.assertEqual(self.new_user.username, "Faith")
        self.assertEqual(self.new_user.password, "Kwamboka@")


if __name__ == '__main__':
    unittest.main()
