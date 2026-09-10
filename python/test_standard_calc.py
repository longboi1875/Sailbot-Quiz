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
