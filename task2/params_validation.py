from datetime import datetime

import pandas as pd

# валидация дат
def validate_dates(date_str, period, freq, chosen_day_str, chosen_week_start_str, chosen_week_finish_str):
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Ошибка: Формат начальной даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
        exit(1)

    try:
        chosen_day = datetime.strptime(chosen_day_str, '%Y-%m-%d')
    except ValueError:
        print("Ошибка: Формат выбранной даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
        exit(1)

    try:
        chosen_week_start = datetime.strptime(chosen_week_start_str, '%Y-%m-%d')
    except ValueError:
        print("Ошибка: Формат начала недели должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
        exit(1)

    try:
        chosen_week_finish = datetime.strptime(chosen_week_finish_str, '%Y-%m-%d')
    except ValueError:
        print("Ошибка: Формат конца недели должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
        exit(1)

    if chosen_week_start >= chosen_week_finish:
        print("Ошибка: Дата начала недели должна быть раньше даты конца недели")
        exit(1)

    dates = pd.date_range(start=start_date, periods=period, freq=freq)

    if chosen_day not in dates:
        print(f"Ошибка: Выбранная дата {chosen_day} отсутствует в массиве дат")
        exit(1)

    if chosen_week_start not in dates:
        print(f"Ошибка: Дата начала недели {chosen_week_start} отсутствует в массиве дат")
        exit(1)
        
    if chosen_week_finish not in dates:
        print(f"Ошибка: Дата конца недели {chosen_week_finish} отсутствует в массиве дат")
        exit(1)

    return start_date, chosen_day, chosen_week_start, chosen_week_finish

# валидация всего остального
def validate_frequency_and_period(freq, period):
    valid_freqs = ['D', 'W', 'M']
    if freq not in valid_freqs:
        print(f"Ошибка: Частота может быть {valid_freqs}")
        exit(1)

    if period <= 0:
        print("Ошибка: Введите адекватное количество дат, пожалуйста")
        exit(1)