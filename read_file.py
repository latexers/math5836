from numpy import genfromtxt
import pandas as pd
data_in = genfromtxt('E:\\Projects\\math5836\\week1\\exercise\\Exercise1.4-PartI\\ENB2012_data.csv', delimiter=",") # in case of csv data
data_csv = pd.read_csv('E:\\Projects\\math5836\\week1\\exercise\\Exercise1.4-PartI\\ENB2012_data.csv')
data_csv = pd.read_excel("")
print(data_csv)