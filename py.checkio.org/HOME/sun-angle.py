from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    """
    Sun angle: 06:00 = 0, 12:00 = 90, 18:00 = 180, 18:01 - 05:59 = "I don't see the sun!"
    :param time: 00:00 - 23:59
    :return: sun angle
    """
    hours, mins = time.split(':')
    total_mins = int(hours) * 60 + int(mins) - 360
    return "I don't see the sun!" if total_mins < 0 or total_mins > 720 else round(total_mins / 4, 2)


print(sun_angle("05:59"))
print(sun_angle("07:00"))
print(sun_angle("12:15"))
print(sun_angle("20:15"))

"""
Best "Clear" Solution:

def sun_angle(time):
    h, m = list(map(int, time.split(':')))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"
"""