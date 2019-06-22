import re
import decimal
def sun_angle(time):
    #replace this for solution
    clock_time = re.match(r"(\d\d):(\d\d)",time)
    time_hour = int(clock_time.group(1))
    time_min = int(clock_time.group(2))
    minuts = (time_hour - 6) * 60 + time_min
    if minuts < 0 or minuts > 720:
        return "I don't see the sun!"
    angle = decimal.Decimal(str(minuts * 0.25))
    #print(time_hour,time_min)
    angle = angle.quantize(decimal.Decimal("10.00"))
    if angle % int(angle) == 0:
        return int(angle)
    return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("12:15"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")