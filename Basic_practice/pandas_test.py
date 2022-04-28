#pip install pandas

import pandas as pd

gapminder = pd.read_csv('https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv')
print(type(gapminder))
print(gapminder.head())


