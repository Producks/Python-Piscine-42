import time
from datetime import date

print("Seconds since January 1, 1970: {} or {:e}\n{}".format(format(time.time(), ","), time.time(), date.today()))