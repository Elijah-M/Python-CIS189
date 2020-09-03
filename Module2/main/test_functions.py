import unittest
from camper_age_input import age_in_years


class FunctionTestCase(unittest.TestCase):
    def test_age(self):
        self.assertEqual(age_in_years, 3)


if __name__ == '__main__':
    unittest.main()