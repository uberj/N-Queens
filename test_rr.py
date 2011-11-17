from rr import *
import unittest

class TestnQueens(unittest.TestCase):
    def setUp(self):
        self.n = 11
        self.two = [[1,2],[3,4]]
        self.two_reflect = [[3,4],[1,2]]
        self.r_90two = [[2,4],[1,3]]
        self.three = [[1,2,3],[4,5,6],[7,8,9]]
        self.three_reflect = [[7,8,9],[4,5,6],[1,2,3]]
        self.r_90three = [[3,6,9],[2,5,8],[1,4,7]]
        self.four =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        self.four_reflect = [[13,14,15,16],[9,10,11,12],[5,6,7,8],[1,2,3,4]]
        self.r_90four = [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]

    def test_rotate901(self):
        self.assertEqual(rotate90(self.two,2),self.r_90two)

    def test_rotate902(self):
        self.assertEqual(rotate90(self.three,3),self.r_90three)

    def test_rotate903(self):
        self.assertEqual(rotate90(self.four,4),self.r_90four)

    def test_reflect1(self):
        self.assertEqual(reflect(self.two,2),self.two_reflect)

    def test_reflect2(self):
        self.assertEqual(reflect(self.three,3),self.three_reflect)

    def test_reflect3(self):
        self.assertEqual(reflect(self.four,4),self.four_reflect)

if __name__ == "__main__":
    unittest.main()

