class Clock(object):
    def __init__(self, hour, minute):
        """
        The constructor function of the class.
        """
        x, self.hour = divmod(hour, 24)
        y, self.minute = divmod(minute, 60)
        self.hour += y

    def __repr__(self):
        """
        Returns the clock time as a string
        """
        return "{}:{}".format(self.hour, self.minute)

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        """Add minutes to an existing clock."""

    def __sub__(self, minutes):
        """Subtract minutes from an existing clock."""


c1 = Clock(23, 59)

print(c1)
