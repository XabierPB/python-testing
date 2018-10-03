from functions.examples.division import division
from nose.tools import raises
from hypothesis import given, assume
from hypothesis.strategies import integers, floats, one_of
import pytest
import unittest


class TestDivision(unittest.TestCase):

    #### Simple ####

    def test_div(self):
        """Test numbers and strings"""
        assert division(4, 2.0) == division('4', '2.0')
        """Test invalid value"""
        assert division(4, 3) != 9

    @raises(ZeroDivisionError)
    def test_divzero_nosetest(self):
        """Test division by zero"""
        division('4', 0)

    def test_divzero_pytest(self):
        """Test division by zero"""
        with pytest.raises(ZeroDivisionError):
            division(4, 0)


    ##### More simple tests ####
    # TODO: Change yield with parametrize
    def test_div_range(self):
        """Test with more numbers and string combinations"""
        for i in range(1, 2):
            yield division, i*2, i
            yield division, float(i*2), i
            yield division, i*2, float(i)
            yield division, float(i*2), float(i)
            yield division, i*2, str(i)
            yield division, str(i*2), i
            # and so forth...

    #### Add given annotation ####

    @given(x=integers())
    def test_div_given(self, x):
        """Test non-zero integers"""
        assume(x is not 0)
        assert division(x*2, x) == 2.0

    #### Add floats too ####

    @given(one_of(integers(), floats()))
    def test_div_multiple_given(self, x):
        """Test integers and floats."""
        assume(x != 0 and x != 0.0)
        assert division(x*2, x) == 2.0


if __name__ == '__main__':
    unittest.main()
