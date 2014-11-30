Dates
=====

Most of the date work you do in Python will involve the datetime module. In
it, we have access to the timedelta module which allows us to calculate time
between dates::

    >>> from datetime import timedelta
    >>> a = timedelta(days=2, hours=6)
    >>> b = timedelta(hours=4.5)
    >>> c = a + b
    >>> print(c.days)
    2
    >>> print(c.seconds)
    37800
    >>> print(c.seconds / 3600)
    10.5
    >>> print(c.total_seconds() / 3600)
    58.5

Of course we can create our own dates as well and manipulate them with this::

    >>> from datetime import datetime
    >>> a = datetime(2012, 9, 23)
    >>> print(a + timedelta(days=10))
    2012-10-03 00:00:00
    >>> b = datetime(2012, 12, 21)
    >>> d = b - a
    >>> print(d.days)
    89
    >>> now = datetime.today()
    >>> print(now)
    2014-11-30 10:15:53.101656
    >>> print(now + timedelta(minutes=10))
    2014-11-30 10:25:53.101656

When the timedelta fails (for months for instance), we have access to the
relativedelta module which takes into account number of days in a month and
all::

    >>> from dateutil.relativedelta import relativedelta
    >>> a + relativedelta(months=+1)
    datetime.datetime(2012, 10, 23, 0, 0)
    >>> a + relativedelta(months=+4)
    datetime.datetime(2013, 1, 23, 0, 0)
    >>>
    >>> # Time between two dates
    >>> b = datetime(2012, 12, 21)
    >>> d = b - a
    >>> d
    datetime.timedelta(89)
    >>> d = relativedelta(b, a)
    >>> d
    relativedelta(months=+2, days=+28)
    >>> d.months
    2
    >>> d.days
    28

The dateutil package can be found when you pip install python-dateutil. If we
want to write a function for finding a day last week based on the day name, we
have some work to do as we need to write a function::

    >>> from datetime import datetime, timedelta
    >>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    ...             'Sunday']
    >>>
    >>> def get_previous_byday(dayname, start_date=None):
    ...     if start_date is None:
    ...         start_date = datetime.today()
    ...     day_num = start_date.weekday()
    ...     day_num_target = weekdays.index(dayname)
    ...     days_ago = (7 + day_num - day_num_target) % 7
    ...     if days_ago == 0:
    ...         days_ago = 7
    ...     target_date = start_date - timedelta(days=days_ago)
    ...     return target_date
    ...
    >>> print(get_previous_byday('Monday'))
    2014-11-24 10:26:14.136691
    >>> print(get_previous_byday('Tuesday'))
    2014-11-25 10:26:14.137300
    >>> print(get_previous_byday('Sunday'))
    2014-11-23 10:26:14.137833

This shows off some things in the datetime module and how you can combine
ideas to come up with smart solutions. We can however makes our lives easier
with the python-dateutil module again::

    >>> from datetime import datetime
    >>> from dateutil.relativedelta import relativedelta
    >>> from dateutil.rrule import *
    >>> d = datetime.now()
    >>> print(d)
    2012-12-23 16:31:52.718111
    >>> # Next Friday
    >>> print(d + relativedelta(weekday=FR))
    2012-12-28 16:31:52.718111
    >>>
    >>> # Last Friday
    >>> print(d + relativedelta(weekday=FR(-1)))
    2012-12-21 16:31:52.718111

And when we want to find all the dates in a month::

    >>> from datetime import datetime, date, timedelta
    >>> import calendar
    >>>
    >>> def get_month_range(start_date=None):
    ...     if start_date is None:
    ...         start_date = date.today().replace(day=1)
    ...     _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    ...     end_date = start_date + timedelta(days=days_in_month)
    ...     return (start_date, end_date)
    ...
    >>> a_day = timedelta(days=1)
    >>> first_day, last_day = get_month_range()
    >>> while first_day < last_day:
    ...     print(first_day)
    ...     first_day += a_day
    ...
    2014-11-01
    2014-11-02
    2014-11-03
    ...

When we have strings though, we can also use the datetime module to convert
them to proper dates::

    >>> from datetime import datetime
    >>> text = '2012-09-20'
    >>> y = datetime.strptime(text, '%Y-%m-%d')
    >>> z = datetime.now()
    >>> diff = z - y
    >>> print(diff)
    801 days, 10:36:38.732114
    >>> nice_z = datetime.strftime(z, '%A %B %d, %Y')
    >>> print(nice_z)
    Sunday November 30, 2014

As it stands, strptime() is slow because it's pure python. It can be better to
manually convert strings by splitting on delimieters, casting to an int, and
building a datetime. This method is 7 times faster than the strptime()
function.

When working with timezones, it's best to use the pytz module for all timezone
work as shown
`here <https://github.com/dansackett/learning-playground/tree/master/python/python-cookbook/chapter_3/code/dates_example.py>`_
