import pandas as pd
import matplotlib.pyplot as plt

# класс для вывода информации о выбранном дне и выбранной неделе
class DateInfo:
    def __init__(self, date, freq, period, chosen_day, chosen_week_start, chosen_week_finish):
        self.date = date
        self.freq = freq
        self.period = period
        self.dates = pd.date_range(start=date, periods=period, freq=freq)
        self.df = pd.DataFrame({
                    'value': range(period)
        }, index=self.dates)
        self.chosen_day = chosen_day
        self.chosen_week_start = chosen_week_start
        self.chosen_week_finish = chosen_week_finish

    def print_day(self):
        chosen_day_info = self.df.loc[self.chosen_day]
        print("-------------------------------------------------------------")
        print(f"Данные за {self.chosen_day}: ")
        print(chosen_day_info)
        print("-------------------------------------------------------------")

    def print_week(self):
        chosen_week_info = self.df.loc[self.chosen_week_start:self.chosen_week_finish]
        print("-------------------------------------------------------------")
        print(f"Данные за {self.chosen_week_start} - {self.chosen_week_finish}: ")
        print(chosen_week_info)
        print("-------------------------------------------------------------")

