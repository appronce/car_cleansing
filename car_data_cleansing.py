import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

car = pd.read_csv(r'C:\Users\IGOR\Desktop\python\vehicles.csv')

# print(car.info())
# print(car.shape)
# print(car.isnull().sum())
# print(car.price.describe())
# print(car['price'].value_counts().iloc[:5])

#plt.figure(figsize=(5,8))
#sns.boxplot(y='price', data=car, showfliers=True)
#plt.show()

car.drop(['description', 'county', 'url', 'region_url', 'image_url', 'posting_date'], axis=1, inplace=True)
car.drop(car[car.price > 300000].index, inplace=True)
car.drop(car[car.price == 0].index, inplace=True)
car.drop_duplicates()
car = car[car.isnull().sum(axis=1) <= 2]
car.to_csv('car_info.csv', index=False)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/car_db')
df = pd.read_csv(r'C:\Users\IGOR\PycharmProjects\program\car_info.csv')

df.to_sql('car', engine, if_exists='replace', index=False)







