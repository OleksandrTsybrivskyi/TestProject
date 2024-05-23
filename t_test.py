import t
import pytest

@pytest.mark.parametrize(
        ("input_n", "expected"),
        (
            (5, 25),
            (3., 9.),
        )
)

def test_square(input_n, expected):
    assert t.square(input_n) == expected

def test_square_float():
    assert t.square(3.) == pytest.approx(9.)

class TestSquare:
    def test_square(self):
        assert t.square(3) == 9 