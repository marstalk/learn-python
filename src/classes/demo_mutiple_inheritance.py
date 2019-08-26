"""Multiple Inheritance


Some classes may derive from multiple classes. This means that the derived class would have its attribute, along with the
attributes of allthe classes that it was derived from.
"""

def test_multiple_inheritance():
    """Multiple inheritance"""

    class Clock:
        time = '11:23 PM'

        def get_time(self):
            return self.time


    class Calendar:
        date = "12/08/2018"

        def get_date(self):
            return self.date

    class CalendarClock(Calendar, Clock):
        pass


    calendarClock = CalendarClock()

    assert calendarClock.get_date() == "12/08/2018"
    assert calendarClock.get_time() == "11:23 PM"




