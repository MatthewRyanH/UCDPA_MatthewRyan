import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pop = pd.read_csv(r"Project CSV/Populations World Bank.csv",
                  index_col=0, )
alc = pd.read_csv(
    r"Project CSV/Alcohol per capita consumption GHO.csv",
    index_col=0, skiprows=2)
tob = pd.read_csv(r"Project CSV/Tobacco consumption GHO.csv",
                  index_col=0, skiprows=1)
life = pd.read_csv(r"Project CSV/Life expectancy GHO.csv",
                   index_col=0, skiprows=1)

pop_df = pd.DataFrame(pop, columns=['2000', '2005', '2010', '2015', '2019', '2020'])
pop_df.sort_values(by=['2000'], inplace=True, ascending=True)
pop_df = pop_df.fillna(0)

alc_df = pd.DataFrame(alc)



life_real = life.iloc[0:, :2]
rl_df = pd.DataFrame(life_real)


for val in pop_df.iterrows():
    print(val)

tob_df = pd.DataFrame(tob, columns=[' Both sexes'])

dftab = pd.merge(tob_df, rl_df, left_index=True, right_index=True)
print(dftab)


def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

avg_sk = tob_df.mean(axis=0, numeric_only=True)
print(avg_sk)
print(rl_df)

pop_df.plot()
alc_df.plot()
rl_df.plot()
tob_df.plot()
plt.show()

