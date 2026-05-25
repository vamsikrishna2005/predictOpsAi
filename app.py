import pandas as pd

df = pd.read_csv("C:\\Users\\vvams\\OneDrive\\Desktop\\exf server monitering\\logging_monitoring_anomalies.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())