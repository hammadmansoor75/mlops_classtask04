# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


df=pd.read_csv('tmdb_5000_movies.csv')
df.head(3)
df.info()
df['original_title'].unique()
df.sort_values(by=['vote_average'])
vt=df.sort_values(by=['vote_average'])
vt.tail(5)
filtre=df['production_countries'].str.contains("TR")
df[filtre]
filtre2=df['production_countries'].str.contains("US")
df[filtre2]
us=df[filtre2]
us['vote_average'].mean()
df[['popularity']].plot()
df['status'].value_counts()
tl=df.groupby(by=['original_title']).mean(numeric_only=True)
tl.loc[["Avatar","Sherlock Holmes","Star Wars"]]
tl.style.background_gradient(cmap="CMRmap_r")
print("COMPLETED")