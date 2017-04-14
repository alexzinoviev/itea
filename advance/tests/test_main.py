import unittest
import unittest.mock
from advance.tests import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.m = main.Maxer([1,2,3])
        print('SetUp')

    @unittest.mock.patch('advance.tests.main.f')
    def testMax1(self, a):
        print(a)
        a.side_effect = [0]
        self.assertEqual(self.m.max(), 3, 'max(1,2,3)')
        print(self.m)


    def testMax2(self):
        self.m.append(5)
        self.assertEqual(self.m.max(), 5)


    def tearDown(self):
        print('Tear Down')