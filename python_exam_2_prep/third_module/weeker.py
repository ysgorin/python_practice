# weeker.py

class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # The class constructor accepts one argument – a
    # string. The string represents the name of the 
    # day of the week and the only acceptable values
    # must come from the following set:
    # Mon Tue Wed Thu Fri Sat Sun
    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        self.__day_index = Weeker.__days.index(day)

    def __str__(self):
        return Weeker.__days[self.__day_index]

    def add_days(self, n):
        self.__day_index = (self.__day_index + n) % 7

    def subtract_days(self, n):
        # Reuse add_days code and turn n into a negative number
        self.add_days(-n)

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
