from __future__ import print_function

import datetime


def add_months(datetime1, n=1):
    one_day = datetime.timedelta(days=1)
    q, r = divmod(datetime1.month + n, 12)
    datetime2 = datetime.datetime(datetime1.year + q, r + 1, 1, hour=datetime1.hour,
                                  minute=datetime1.minute,
                                  second=datetime1.second,
                                  microsecond=datetime1.microsecond) - one_day
    '''
        if datetime1 day is bigger than last day of
        target month, then, use datetime2
        for example: datetime1 = 10.31 datetime2 = 11.30
    '''
    if datetime1.day >= datetime2.day:
        return datetime2
    return datetime2.replace(day=datetime1.day)


if __name__ == "__main__":
    sday = datetime.datetime.strptime('20170731122350', '%Y%m%d%H%M%S')
    print(add_months(sday, -1))
    for i in range(0, 100):
        print(add_months(sday, -i))








