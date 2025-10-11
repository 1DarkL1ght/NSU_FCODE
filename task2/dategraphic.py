import pandas as pd
import matplotlib.pyplot as plt

# класс для сохранения графика периода дат
class DateGraphic:
    def __init__(self, date, freq, period, filename):
        self.date = date
        self.freq = freq
        self.period = period
        self.dates = pd.date_range(start=date, periods=period, freq=freq)
        self.df = pd.DataFrame({
                    'value': range(period)
        }, index=self.dates)
        self.df_with_missings = self.df.copy()
        self.graphic = None
        self.filename = filename


    def add_missing_values(self, num_missings: int=1):
        """
        Adds missing values to the copy of the DataFrame.
        """
        if num_missings < 1:
            raise ValueError("Количество пропусков должно быть больше нуля")
        
        # Добавляем пропуски в случайные места
        for _ in range(num_missings):
            idx = self.df_with_missings.sample().index[0]
            self.df_with_missings.loc[idx] = None

        print(f"Добавлено {num_missings} пропусков в данные")


    def interpolate_missing_values(self):
        """
        Interpolates missing valeus in the DataFrame copy.
        """
        self.df_with_missings['value'] = self.df_with_missings['value'].interpolate(method='linear')
        print("Пропуски в данных заполнены линейной интерполяцией")


    def save_graphic(self):
        def calculate_mae():
            return (self.df['value'] - self.df_with_missings['value']).abs().mean()
        
        plt.plot(self.df.index, self.df['value'], marker='o', linestyle='-', color='blue', label='Исходные данные')
        plt.plot(self.df_with_missings.index, self.df_with_missings['value'], marker='x', linestyle='--', color='orange', label='Интерполяция пропусков')
        plt.title(f'MAE: {calculate_mae():.2f}')
        plt.grid(True)
        plt.xticks(rotation=60)
        plt.tight_layout()
        plt.savefig(f'{self.filename}.png')
        plt.close()

        print(f"График сохранён в файл '{self.filename}.png'")        

