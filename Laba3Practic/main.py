import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Python\Laba3Practic\playstation_players.csv")
country_couter = data['country'].value_counts()
plt.pie(country_couter.values, labels = country_couter.index)
plt.show()