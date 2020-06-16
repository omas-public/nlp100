import unittest
import ch1


class Test(unittest.TestCase):
    def test_f00(self):
        str = 'desserts'
        self.assertEqual(str, ch1.f00())

    def test_f01(self):
        str = 'タクシー'
        self.assertEqual(str, ch1.f01())
    
    def test_f02(self):
        str = 'パタトクカシーー'
        self.assertEqual(str, ch1.f02())

    def test_f03(self):
        list = [3,1,4,1,5,9,2,6,5,3,5,8,8,7,9]
        self.assertEqual(list, ch1.f03())

    def test_f04(self):
        dict = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
        self.assertEqual(dict, ch1.f04())

    def test_f05(self):
        list = [['Iam', 'aman', 'anNLPer'], ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']]
        self.assertEqual(list, ch1.f05())

    # def test_f05_word_bigram(self):
    #     matrix = [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    #     self.assertEqual(matrix, ch1.f05_word_bigram())

    # def test_f05_char_bigram(self):
    #     list = ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
    #     self.assertEqual(matrix, ch1.f05_word_bigram())

    def test_f07(self):
        str = '12時の気温は22.4'
        self.assertEqual(str, ch1.f07())

    def test_f08(self):
        str = 'Hvool dliow!'
        self.assertEqual(str, ch1.f08())

if __name__ == "__main__":
    unittest.main()
