import unittest
from AnLinq import AnLinq


class TestAnLinq(unittest.TestCase):
    def setUp(self):
        self.number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.number_array_duplicates = [3, 2, 1, 3, 2, 1, 5]
        self.number_array_duplicates_distinct = [3, 2, 1, 5]
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

    def test_iter(self):
        self.assertEqual(AnLinq(self.number_array)[0], self.number_array[0])
        self.assertEqual(AnLinq(self.number_array)[1], self.number_array[1])
        self.assertEqual(AnLinq(self.word_array)[1], self.word_array[1])
        self.assertEqual(AnLinq(self.word_array)[1], self.word_array[1])
        try:
            AnLinq(self.number_array)[100]
            self.assertTrue(False, "Must raise AnLinqException before this line")
        except AnLinq.AnLinqException:
            pass
        try:
            AnLinq([])[0]
            self.assertTrue(False, "Must raise AnLinqException before this line")
        except AnLinq.AnLinqException:
            pass

    def test_len(self):
        self.assertEqual(len(AnLinq(self.number_array)), len(self.number_array))
        self.assertEqual(len(AnLinq(self.object_array)), len(self.object_array))
        self.assertEqual(len(AnLinq([])), 0)

    def test_for(self):
        count = 0
        for item in AnLinq(self.number_array):
            self.assertEqual(item, self.number_array[count])
            count += 1

        for item in AnLinq([]):
            self.assertTrue(False, "Should not hit this line")

    def test_equals(self):
        self.assertEqual(AnLinq(self.number_array), AnLinq(self.number_array))
        self.assertEqual(AnLinq(self.number_array), self.number_array)
        self.assertNotEqual(AnLinq(self.number_array), AnLinq(self.number_array_duplicates_distinct))
        self.assertEqual(AnLinq(self.number_array).where(lambda x: True), self.number_array)
        self.assertEqual(AnLinq(self.number_array).where(lambda x: True).distinct(), self.number_array)
        self.assertEqual(AnLinq(self.number_array).where(lambda x: False), [])
        self.assertEqual(AnLinq(self.number_array).where(lambda x: False).distinct(), [])

    def test_any(self):
        self.assertTrue(AnLinq(self.number_array).any(lambda x: x == 0))
        self.assertTrue(AnLinq(self.number_array).any(lambda x: x == 4))
        self.assertTrue(AnLinq(self.number_array).any(lambda x: x > 0))
        self.assertTrue(AnLinq(self.number_array).any(lambda x: x >= 9))
        self.assertTrue(AnLinq(self.object_array).any(lambda x: x['name'] == 'Julia'))

        self.assertFalse(AnLinq([]).any(lambda x: True))
        self.assertFalse(AnLinq([]).any(lambda x: False))
        self.assertFalse(AnLinq(self.number_array).any(lambda x: x > 9))
        self.assertFalse(AnLinq(self.number_array).any(lambda x: x < 0))
        self.assertFalse(AnLinq(self.number_array).any(lambda x: x < 0))
        self.assertFalse(AnLinq(self.object_array).any(lambda x: x['name'] == 'Freddie'))

    def test_all(self):
        self.assertTrue(AnLinq(self.number_array).all(lambda x: x >= 0))
        self.assertTrue(AnLinq(self.word_array).all(lambda x: len(x) > 2))
        self.assertTrue(AnLinq([]).all(lambda x: True))
        self.assertTrue(AnLinq([]).all(lambda x: False))

        self.assertFalse(AnLinq(self.number_array).all(lambda x: x == 0))
        self.assertFalse(AnLinq(self.number_array).all(lambda x: x == 4))
        self.assertFalse(AnLinq(self.number_array).all(lambda x: x > 0))
        self.assertFalse(AnLinq(self.number_array).all(lambda x: x >= 9))
        self.assertFalse(AnLinq(self.number_array).all(lambda x: x > 9))
        self.assertFalse(AnLinq(self.number_array).all(lambda x: x < 0))
        self.assertFalse(AnLinq(self.object_array).all(lambda x: x['name'] == 'Julia'))
        self.assertFalse(AnLinq(self.object_array).all(lambda x: x['name'] == 'Freddie'))

    def test_first(self):
        self.assertEqual(AnLinq(self.number_array).first(), self.number_array[0])
        self.assertEqual(AnLinq(self.number_array).first(lambda x: x > 3), 4)
        self.assertEqual(AnLinq(self.number_array).first(lambda x: x == 0), 0)
        try:
            AnLinq(self.number_array).first(lambda x: x == 12321)
            self.assertTrue(False)
            self.assertTrue(False, "Must raise AnLinqException before this line")
        except AnLinq.AnLinqException:
            pass

    def test_first_or_none(self):
        self.assertEqual(AnLinq(self.number_array).first_or_none(), self.number_array[0])
        self.assertEqual(AnLinq(self.number_array).first_or_none(lambda x: x > 3), 4)
        self.assertEqual(AnLinq(self.number_array).first_or_none(lambda x: x == 0), 0)
        self.assertEqual(AnLinq(self.number_array).first_or_none(lambda x: x == 12321), None)

    def test_last(self):
        self.assertEqual(AnLinq(self.number_array).last(), self.number_array[-1])
        self.assertEqual(AnLinq(self.number_array).last(lambda x: x > 3), 9)
        self.assertEqual(AnLinq(self.number_array).last(lambda x: x == 0), 0)
        try:
            AnLinq(self.number_array).last(lambda x: x == 12321)
            self.assertTrue(False, "Must raise AnLinqException before this line")
        except AnLinq.AnLinqException:
            pass

    def test_last_or_none(self):
        self.assertEqual(AnLinq(self.number_array).last_or_none(), self.number_array[-1])
        self.assertEqual(AnLinq(self.number_array).last_or_none(lambda x: x > 3), 9)
        self.assertEqual(AnLinq(self.number_array).last_or_none(lambda x: x == 0), 0)
        self.assertEqual(AnLinq(self.number_array).last_or_none(lambda x: x == 12321), None)

    def test_to_list(self):
        self.assertEqual(AnLinq(self.number_array).to_list(), self.number_array)
        self.assertEqual(AnLinq(self.number_array).to_list(), AnLinq([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]).to_list())
        self.assertEqual(AnLinq(self.word_array).to_list(), self.word_array)
        self.assertEqual(AnLinq(self.object_array).to_list(), self.object_array)

    def test_to_dictionary(self):
        self.assertDictEqual(AnLinq(self.number_array).to_dictionary(),
                             {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 0: 0})
        self.assertDictEqual(AnLinq(self.number_array).to_dictionary(lambda x: '#' + repr(x)),
                             {'#1': 1, '#2': 2, '#3': 3, '#4': 4, '#5': 5, '#6': 6, '#7': 7, '#8': 8, '#9': 9, '#0': 0})
        self.assertDictEqual(AnLinq(self.number_array).to_dictionary(None, lambda x: '#' + repr(x)),
                             {1: '#1', 2: '#2', 3: '#3', 4: '#4', 5: '#5', 6: '#6', 7: '#7', 8: '#8', 9: '#9', 0: '#0'})
        self.assertDictEqual(AnLinq(self.number_array).to_dictionary(lambda x: '#' + repr(x), lambda x: '#' + repr(x)),
                             {'#1': '#1', '#2': '#2', '#3': '#3', '#4': '#4', '#5': '#5',
                              '#6': '#6', '#7': '#7', '#8': '#8', '#9': '#9', '#0': '#0'})
        try:
            AnLinq(self.number_array_duplicates).to_dictionary(None, None, True)
            self.assertTrue(False, "Must raise AnLinqException before this line")
        except AnLinq.AnLinqException:
            pass

        self.assertDictEqual(AnLinq(self.number_array_duplicates).to_dictionary(None, None, False),
                             {3: 3, 2: 2, 1: 1, 5: 5})

    def test_where(self):
        self.assertEqual(AnLinq(self.number_array).where(lambda x: True).to_list(), self.number_array)
        self.assertEqual(AnLinq(self.number_array).where(lambda x: False).to_list(), [])
        self.assertEqual(AnLinq(self.number_array).where(lambda x: x > 3).to_list(), [4, 5, 6, 7, 8, 9])
        self.assertEqual(AnLinq(self.number_array).where(lambda x: x < 3).to_list(), [1, 2, 0])
        self.assertEqual(AnLinq(self.word_array).where(lambda x: len(x) <= 4).to_list(), ['RED', 'BLUE'])
        self.assertEqual(AnLinq(self.word_array).where(lambda x: len(x) == 6).to_list(),
                         ['ORANGE', 'YELLOW', 'INDIGO', 'VIOLET'])
        self.assertEqual(AnLinq(self.word_array)
                         .where(lambda x: len(x) > 3)
                         .where(lambda x: len(x) < 6).to_list(), ['GREEN', 'BLUE'])
        self.assertEqual(AnLinq(self.word_array)
                         .where(lambda x: False)
                         .where(lambda x: True).to_list(), [])
        self.assertEqual(AnLinq(self.object_array).where(lambda x: x['born'] > 1990).to_list(), [self.object_array[1]])

    def test_distinct(self):
        self.assertEqual(AnLinq([]).distinct().to_list(), [])
        self.assertEqual(AnLinq(self.number_array).distinct().to_list(), self.number_array)
        self.assertEqual(AnLinq(self.number_array_duplicates).distinct().to_list(),
                         self.number_array_duplicates_distinct)
        self.assertEqual(AnLinq(self.number_array)
                         .distinct(lambda x: 'one key for all').to_list(), [1])
        self.assertEqual(AnLinq(self.number_array)
                         .distinct(lambda x: 'even' if x % 2 == 0 else 'odd').to_list(), [1, 2])

    def test_group_by(self):
        self.assertDictEqual(AnLinq(self.number_array).group_by(),
                             {1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8], 9: [9], 0: [0]})

        self.assertDictEqual(AnLinq(self.number_array).group_by(lambda x: 'even' if x % 2 == 0 else 'odd'),
                             {'even': [2, 4, 6, 8, 0], 'odd': [1, 3, 5, 7, 9]})

    def test_map(self):
        self.assertEqual(AnLinq(self.number_array).map(lambda x: '#' + repr(x)),
                         ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#0'])

    def test_reduce(self):
        self.assertEqual(AnLinq(self.number_array).reduce(lambda prev, this, index: prev + this, 0), 45)
        self.assertEqual(AnLinq(self.number_array).reduce(lambda prev, this, index: prev + this, -1), 44)

if __name__ == '__main__':
    unittest.main()