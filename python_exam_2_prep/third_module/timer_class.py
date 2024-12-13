# timer_class.py

# Scenario
# We need a class able to count seconds. 

# Expected output
# 23:59:59
# 00:00:00
# 23:59:59

class Timer: # The name of the class is Timer
    # Its
    # constructor accepts three arguments
    # representing hours (a value from range [0..23]
    # - we will be using the military time), minutes
    # (from range [0..59]) and seconds (from range
    # [0..59]).
    # Zero is the default value for all of the above
    # parameters. There is no need to perform any
    # validation checks.
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours = (self.__hours + 1) % 24

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours = (self.__hours - 1) % 24

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)