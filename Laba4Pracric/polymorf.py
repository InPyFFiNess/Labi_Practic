import pandas as pd

class DataSet:
    def __init__(self):
        self.data = pd.read_csv('var8.csv')
        self.df = self.data.copy() 

    def __pos__(self):
        a = self.df.shape[0] #Изначально
        self.df = self.df.drop_duplicates()
        b = self.df.shape[0] #Без дубликатов
        deletion = a - b
        print(f'В файле удалено дубликатов: {deletion}')

    def divide(self):
        df1 = self.df[self.df['Результат операции'] == 'успешно'] 
        df2 = self.df[self.df['Результат операции'] == 'недостаточно средств']   
        df3 = self.df[self.df['Результат операции'] == 'неправильный ввод пин-кода']
        
        df1.to_csv('first.csv', index=False)
        df2.to_csv('second.csv', index=False)
        df3.to_csv('third.csv', index=False)

    def __del__(self):
        print('Запрос выполнен')

