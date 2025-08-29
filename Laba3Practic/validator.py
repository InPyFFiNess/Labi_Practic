from datetime import datetime as dt
import pandas as pd
import getpass
from functools import wraps

def log_decorator(log_file = r"D:\Python\Laba3Practic\logs.csv"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_data = {
                'id': 1,
                'pc_username': getpass.getuser(),
                'function_name': func.__name__,
                'date':dt.now().strftime("%d.%m.%Y"),
                'time':dt.now().strftime("%H:%M:%S")
            }
            log_df = pd.DataFrame([log_data])
            try:
                existing_logs = pd.read_csv(log_file)
            except FileNotFoundError:
                existing_logs = pd.DataFrame()
            combined_logs = pd.concat([existing_logs, log_df])
            combined_logs.to_csv(log_file)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_decorator(r"D:\Python\Laba3Practic\logs.csv")
def calculate_sum(a, b):
    """Простая функция сложения"""
    return a + b

result1 = calculate_sum(5, 3)
print(f"Sum: {result1}")

def view_logs(log_file=r"D:\Python\Laba3Practic\logs.csv"):
    """Функция для просмотра логов"""
    try:
        logs = pd.read_csv(log_file);
        print("Логи вызовов функций:");
        print(logs.to_string(index=False));
        return logs
    except FileNotFoundError:
        print("Файл логов не найден")
        return None

# Использование
view_logs(r"D:\Python\Laba3Practic\logs.csv")



