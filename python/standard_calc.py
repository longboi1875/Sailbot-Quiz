def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    # every angle can be translated by repeatedly adding/subtracting 360
    # first thought was doing it with a while loop until we reached the desired range, 
        # however that is very wasteful, we can do an equivalent thing with mod
        # its still possible for the mod to return a result outside of the range however, so subtracting 360 is required

    angle = angle % 360


    if angle >= 180:
        angle -= 360

    return float(angle)


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    # first_angle and second_angle split the circle into two pieces essentially
    # the reflex angle is the longer distance between them
    # so, middle_angle is between them if its on the shorter path

    #distance between angles (arc concept)
    clockwise_d = (second_angle - first_angle) % 360

    # if the clockwise path is 180 degrees or less, it means clockwise is the shorter arc (not the reflex one)
    if clockwise_d <= 180:
        middle_d = (middle_angle - first_angle) % 360
        return middle_d <= clockwise_d

    # otherwise, the clockwise path is the reflex angle,
    # so the shorter arc must be counterclockwise
    else: 
        ccw_d = (first_angle - second_angle) % 360
        middle_d = (first_angle - middle_angle) % 360
        return middle_d <= ccw_d

