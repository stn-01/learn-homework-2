"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime
"""
import datetime

def print_days():
    print(f"Вчера: {(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d.%m.%Y')}; "
          f"Сегодня: {datetime.datetime.now().strftime('%d.%m.%Y')}; "
          f"30 дней назад: {(datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%d.%m.%Y')}")


def str_2_datetime(date_string):
    date_and_time = date_string.split()
    d, m, y = date_and_time[0].split('/')
    mn, sc, ms_mcs = date_and_time[1].split(':')
    ms, mcs = ms_mcs.split('.')
    return datetime.datetime(int(y)+2000, int(m), int(d), int(mn), int(sc), int(ms), int(mcs))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
