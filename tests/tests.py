import unittest
from anlinq import AnLinq


class TestAnLinq(unittest.TestCase):

    def setUp(self):
        self.number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.word_array = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET']
        self.object_array = [
            {
                'name': 'Masha',
                'born': 1986,
                'hobbies': ['skating', 'reading']
            },
            {
                'name': 'Julia',
                'born': 1992,
                'hobbies': ['dancing']
            },
            {
                'name': 'Morticia',
                'born': 1978,
                'hobbies': ['burial', 'knitting', 'haunting']
            }
        ]


    def test_to_list(self):
        self.assertEqual(AnLinq(self.number_array).to_list(), self.number_array)
        self.assertEqual(AnLinq(self.number_array).to_list(), AnLinq([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]).to_list())
        self.assertEqual(AnLinq(self.word_array).to_list(), self.word_array)
        self.assertEqual(AnLinq(self.object_array).to_list(), self.object_array)

    def test_where(self):
        self.assertEqual(AnLinq(self.number_array).where(lambda x: True).to_list(), self.number_array)
        self.assertEqual(AnLinq(self.number_array).where(lambda x: False).to_list(), [])
        self.assertEqual(AnLinq(self.number_array).where(lambda x: x > 3).to_list(), [4, 5, 6, 7, 8, 9])
        self.assertEqual(AnLinq(self.number_array).where(lambda x: x < 3).to_list(), [1, 2, 0])
        self.assertEqual(AnLinq(self.word_array).where(lambda x: len(x) <= 4).to_list(), ['RED', 'BLUE'])
        self.assertEqual(AnLinq(self.word_array).where(lambda x: len(x) == 6).to_list(), ['ORANGE', 'YELLOW', 'INDIGO', 'VIOLET'])



if __name__ == '__main__':
    unittest.main()