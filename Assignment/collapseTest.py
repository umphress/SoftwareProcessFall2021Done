import unittest
import Assignment.collapse as collapse


class PrimeInRangeTest(unittest.TestCase):

# Happy path test
    def test100_100_ShouldCollapseSingleDigit(self):
        value = '5'
        expectedResult = 5
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
