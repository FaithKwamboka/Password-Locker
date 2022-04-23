import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Faith","kkjjliuyj")
        
    def test_init(self):
        self.assertEqual(self.new_user.username,"Faith")
        self.assertEqual(self.new_user.userpassword,"kkjjliuyj")
    
if __name__ == '__main__':
    unittest.main()   