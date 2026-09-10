from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_positive_angle_in_range():
    assert bound_to_180(135) == 135


def test_positive_angle_out_of_range():
    assert bound_to_180(200) == -160


def test_negative_angle_in_range():
    assert bound_to_180(-90) == -90


def test_negative_angle_out_of_range():
    assert bound_to_180(-200) == 160


def test_one_full_rotation():
    assert bound_to_180(360) == 0


def test_two_full_rotations():
    assert bound_to_180(720) == 0


def test_angle_above_full_rotation():
    assert bound_to_180(450) == 90


def test_angle_below_negative_rotation():
    assert bound_to_180(-450) == -90


def test_positive_180_boundary():
    assert bound_to_180(180) == -180


def test_negative_180_boundary():
    assert bound_to_180(-180) == -180


def test_large_positive_angle():
    assert bound_to_180(1000) == -80


def test_large_negative_angle():
    assert bound_to_180(-1000) == 80


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)

def test_middle_inside_simple():
    assert is_angle_between(0, 45, 90)


def test_middle_outside_simple():
    assert not is_angle_between(0, 120, 90)


def test_wraps_across_zero():
    assert is_angle_between(350, 0, 10)


def test_outside_across_zero():
    assert not is_angle_between(350, 180, 10)


def test_negative_angles():
    assert is_angle_between(-90, -45, 0)


def test_mixed_positive_negative():
    assert is_angle_between(-30, 0, 30)


def test_reflex_side():
    assert not is_angle_between(45, 90, 270)


def test_middle_equals_first():
    assert is_angle_between(30, 30, 100)


def test_middle_equals_second():
    assert is_angle_between(30, 100, 100)


def test_angles_over_360():
    assert is_angle_between(360, 405, 450)


def test_angles_below_negative_360():
    assert is_angle_between(-360, -315, -270)


def test_equivalent_angles():
    assert is_angle_between(0, 360, 90)
