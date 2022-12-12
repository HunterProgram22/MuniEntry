import pytest
from munientry.mainwindow.main_window_slots import update_case_number

TEST_CASE_NUMBERS = [
    ('22TRD00001', '22TRD00001'),
    ('22TRC0012', '22TRC00012'),
    ('21CRB025', '21CRB00025'),
    ('20TRD30', '20TRD00030'),
    ('22CRB1', '22CRB00001'),
    ('21TRC0001', '21TRC00001'),
    ('21CRB20', '21CRB00020'),
    ('20TRD1234', '20TRD01234'),
    ('19TRD004', '19TRD00004'),
    ('18CRB123', '18CRB00123')
]

@pytest.mark.parametrize("test_input, expected_output", TEST_CASE_NUMBERS)
def test_update_case_number(test_input, expected_output):
    """Tests to see if function adds missing 0's to get proper case number format.

    Proper Case Number Format = DDXXXDDDDD (D = Digit, X = Letter)
    """
    assert update_case_number(test_input) == expected_output
