from datetime import datetime, date
import argparse

import pandas as pd

from dategraphic import DateGraphic
from dateinfo import DateInfo
from params_validation import validate_dates, validate_frequency_and_period

# функция для парсинга параметров командной строки
def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--date", type=str, help="Начальная дата в формате ГГГГ-ММ-ДД", default=date.today().strftime('%Y-%m-%d'))
    parser.add_argument("--freq", type=str, help="Частота", default='D')
    parser.add_argument("--period", type=int, help="Количество дат", default=30)
    parser.add_argument("--filename", type=str, default=f"date_graphic_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}")
    parser.add_argument("--chosen_day", type=str, help="Выбранная дата", default=date.today().strftime('%Y-%m-%d'))
    parser.add_argument("--chosen_week_start", type=str, help="Начало выбранной недели", default=date.today().strftime('%Y-%m-%d'))
    parser.add_argument("--chosen_week_finish", type=str, help="Конец выбранной недели", default=(date.today() + pd.Timedelta(days=7)).strftime('%Y-%m-%d'))

    return parser.parse_args()  

# основной код - валидация параметров, создание графика, вывод информации
def main():
    args = parse_arguments()

    start_date, chosen_day, chosen_week_start, chosen_week_finish = validate_dates(
        args.date, args.period, args.freq, args.chosen_day, args.chosen_week_start, args.chosen_week_finish
    )

    validate_frequency_and_period(args.freq, args.period)

    dategraphic = DateGraphic(start_date, args.freq, args.period, args.filename)
    dategraphic.add_missing_values(num_missings=3)
    dategraphic.interpolate_missing_values()
    dategraphic.save_graphic()

    dateinfo = DateInfo(start_date, args.freq, args.period, chosen_day, chosen_week_start, chosen_week_finish)
    dateinfo.print_day()
    dateinfo.print_week()

if __name__ == "__main__":
    main()