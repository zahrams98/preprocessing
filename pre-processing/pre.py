from pandas import read_csv
from pandas import set_option
path = r"C:\pima-indians-diabetes.csv"
headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
set_option('precision', 2)
# print(data.shape)
# print(data[:50])
# print(data.dtypes)
# print(data.describe())
count_class = data.groupby('class').size()
print(count_class)
